## A Thing Called the Stack - 60

### Description

A friend was stacking dinner plates, and handed you this, saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

### Hint

  - Where is the return address saved on the stack?
  - Which commands actually affect the stack?

### Write up

```
foo:
    pushl %ebp
    mov %esp, %ebp
    pushl %edi
    pushl %esi
    pushl %ebx
    sub $0xf8, %esp
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

0x10(4 pushes) + 0xf8 = 0x108

> 0x108
