## Dragon's Horde

### Description

> You are a member of the dragon slayer's guild within your town.
Word comes to the guild of a dragon seen in a nearby mountain range.
You and your party decide to go out and slay the beast.
There is surely great wealth and glory to be obtained.
But be careful, dragons can be tricky creatures to deal with.

### Write up

```
   0x08049251 <+1352>:	mov    DWORD PTR [ebp-0xc],0xa
   0x08049258 <+1359>:	cmp    DWORD PTR [ebp-0xc],0x1
   0x0804925c <+1363>:	je     0x8049263 <main+1370>
   0x0804925e <+1365>:	call   0x8048b0b <_Z4foo1v>
   0x08049263 <+1370>:	mov    DWORD PTR [ebp-0xc],0x14
   0x0804926a <+1377>:	cmp    DWORD PTR [ebp-0xc],0xc
   0x0804926e <+1381>:	je     0x8049275 <main+1388>
   0x08049270 <+1383>:	call   0x8048b2d <_Z4foo2v>
   0x08049275 <+1388>:	mov    DWORD PTR [ebp-0xc],0x36
   0x0804927c <+1395>:	cmp    DWORD PTR [ebp-0xc],0xfffffffd
   0x08049280 <+1399>:	je     0x8049287 <main+1406>
   0x08049282 <+1401>:	call   0x8048b4f <_Z4foo3v>
```

There are some `_Z4foo(NUM)v` functions in main().

But they are not actually executed, since jmp conditions are always true.

```
gdb-peda$ pdisas _Z4foo1v
Dump of assembler code for function _Z4foo1v:
   0x08048b0b <+0>:	push   ebp
   0x08048b0c <+1>:	mov    ebp,esp
   0x08048b0e <+3>:	sub    esp,0x18
   0x08048b11 <+6>:	mov    BYTE PTR [ebp-0x9],0x66
   0x08048b15 <+10>:	movsx  eax,BYTE PTR [ebp-0x9]
   0x08048b19 <+14>:	sub    esp,0x8
   0x08048b1c <+17>:	push   eax
   0x08048b1d <+18>:	push   0x804c190
   0x08048b22 <+23>:	call   0x80489f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLEc@plt>
   0x08048b27 <+28>:	add    esp,0x10
   0x08048b2a <+31>:	nop
   0x08048b2b <+32>:	leave  
   0x08048b2c <+33>:	ret    
End of assembler dump.
gdb-peda$ pdisas _Z4foo2v
Dump of assembler code for function _Z4foo2v:
   0x08048b2d <+0>:	push   ebp
   0x08048b2e <+1>:	mov    ebp,esp
   0x08048b30 <+3>:	sub    esp,0x18
   0x08048b33 <+6>:	mov    BYTE PTR [ebp-0x9],0x6c
   0x08048b37 <+10>:	movsx  eax,BYTE PTR [ebp-0x9]
   0x08048b3b <+14>:	sub    esp,0x8
   0x08048b3e <+17>:	push   eax
   0x08048b3f <+18>:	push   0x804c190
   0x08048b44 <+23>:	call   0x80489f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLEc@plt>
   0x08048b49 <+28>:	add    esp,0x10
   0x08048b4c <+31>:	nop
   0x08048b4d <+32>:	leave  
   0x08048b4e <+33>:	ret    
End of assembler dump.

```

In every `_Z4foo(NUM)v` fucntions, they are doing some string operation with same string and one byte.

By following each `_Z4foo(NUM)v` functions, it can be found that those one bytes are 0x66, 0x6c, 0x61, ... which is `flag{...`

So, by checking all one bytes in each `_Z4foo(NUM)v` functions, we can get the flag

> flag{r3v_1t_up}
