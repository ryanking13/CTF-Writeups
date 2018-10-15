## learn gdb - 300

### Description

> Using a debugging tool will be extremely useful on your missions. Can you run this program in gdb and find the flag? You can find the file in /problems/learn-gdb_1_a2decdea3e89bfcdcbd9de1a67ceed0e on the shell server.

### Write up

```
$ ./run
Decrypting the Flag into global variable 'flag_buf'
.....................................
Finished Reading Flag into global variable 'flag_buf'. Exiting.
```

The program saves flag into `flag_buf` global variable then exits.

```
$ nm run | grep flag_buf
00000000006013e8 B flag_buf
```

flag_buf's address is 0x6013e8

```
gdb-peda$ disas main
...
0x0000000000400905 <+60>:	call   0x400786 <decrypt_flag>
0x000000000040090a <+65>:	mov    edi,0x400a08
...
gdb-peda$ b *main+65
gdb-peda$ r
```

set breakpoint after decrypt_flag function, then run.

```
gdb-peda$ x/x 0x6013e8
0x6013e8 <flag_buf>:	0x10	0x20	0x60	0x00
gdb-peda$ x/s 0x602010
0x602010:	"picoCTF{gDb_iS_sUp3r_u53fuL_f3f39814}"
```
