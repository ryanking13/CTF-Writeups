## core - 350

### Description

> This program was about to print the flag when it died. Maybe the flag is still in this core file that it dumped? Also available at /problems/core_4_0cb5abf1372990e2b85bbe73dec0d95f on the shell server.

### Write up

Binary and core file is given.

By analysing binary, it could be found that, flag strings address is saved strs[1337].

```
0804a080 B strs
```

and strs is at 0x0804a080.

0x0804a080 + (1337 * 4) = 0x0804b564

```
804b563:   08 f0                   or     %dh,%al
804b565:   10 06                   adc    %al,(%esi)
804b567:   08 18                   or     %bl,(%eax)
804b569:   11 06                   adc    %eax,(%esi)
```

Value in 0x0804b564 is 0x080610f0 (litten endian).

```
80610f0:   63 39                   arpl   %di,(%ecx)
80610f2:   36 62 64 30 66          bound  %esp,%ss:0x66(%eax,%esi,1)
80610f7:   61                      popa
80610f8:   32 64 61 35             xor    0x35(%ecx,%eiz,2),%ah
80610fc:   63 30                   arpl   %si,(%eax)
80610fe:   38 35 33 63 66 31       cmp    %dh,0x31666333
8061104:   32 63 34                xor    0x34(%ebx),%ah
8061107:   66 39 33                cmp    %si,(%ebx)
806110a:   66 63 65 32             data16 arpl %sp,0x32(%ebp)
```

flag here!

```
c96bd0fa2da5c0853cf12c4f93fce288
```