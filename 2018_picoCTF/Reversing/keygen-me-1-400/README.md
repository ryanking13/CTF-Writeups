## keygen-me-1 - 400

### Description

> Can you generate a valid product key for the validation program in /problems/keygen-me-1_4_df4d05561b43c5fcd87e7072e1001877

### Write up

```
BOOL __cdecl check_valid_char(char a1)
{
  return a1 > 47 && a1 <= 57 || a1 > 64 && a1 <= 90;
}
```

valid key is length 16 with characters consists of 0-9, A-Z

it uses first 15 bytes to calculate some complicated operation,
and compares the result with 16th byte.

Where comparison happens is on `validate_key+162`.

```
gdb-peda$ r 0000000000000000
Starting program: /csehome/ryanking13/ctf/picoctf2018/keygen/activate 0000000000000000

[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0xc ('\x0c')
ECX: 0xc ('\x0c')
...
[-------------------------------------code-------------------------------------]
   0x8048808 <validate_key+151>:	call   0x80486b8 <ord>
   0x804880d <validate_key+156>:	add    esp,0x10
   0x8048810 <validate_key+159>:	movsx  eax,al
=> 0x8048813 <validate_key+162>:	cmp    ebx,eax

```

By giving 0000000000000000 as the key, the calculated byte is 0xc in ebx, and last byte is 0x0.

If we change last byte to C, then flag is retrieved.

```
$ ./activate 000000000000000C
Product Activated Successfully: picoCTF{k3yg3n5_4r3_s0_s1mp13_3806765070}
```
