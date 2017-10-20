## Programmers Assemble - 75

### Description

You found a text file with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

### Hint

  - All of the commands can be found [here](https://en.wikipedia.org/wiki/X86_assembly_language) along with what they do.
  - It may be useful to be able to run the code, with test values.

### Write up

```
.global main

main:
    mov $XXXXXXX, %eax
    mov $0, %ebx
    mov $0x4, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0x3ca8, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```

Inside the loop, `%ebx = %ebx + 4` happens for %eax time.

And the value of %ebx after the loop must be 0x3ca8 to return 1.

So, %eax must be 0x3ca8 / 0x4 = 0xf2a


> 0xf2a
