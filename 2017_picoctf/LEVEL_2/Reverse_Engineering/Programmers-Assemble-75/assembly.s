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
