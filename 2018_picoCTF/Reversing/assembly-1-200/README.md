## assembly-1 - 200

### Description

> What does asm1(0xc8) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-1_4_99ac7ff5dfe75417ed616e35bfc2c023.

### Write up

```
asm1:
    ...
    cmp DWORD PTR [ebp+0x8],0x9a
    jg  part_a  
```

True, jump

```
part_a:
    cmp DWORD PTR [ebp+0x8],0x2c
    jne part_c
```

True, jump

```
part_c:
    mov eax,DWORD PTR [ebp+0x8]
    add eax,0x3
part_d:
    pop ebp
    ret
```

eax = 0xc8 + 3 = 0xcb