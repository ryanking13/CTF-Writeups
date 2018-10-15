## assembly-0 - 150

### Description

> What does asm0(0xc9,0xb0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-0_4_0f197369bfc00a9211504cf65ac31994.

### Write up

```
.intel_syntax noprefix
.bits 32

.global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp
	ret
```

0xb0 is moved to ebx, ebx is moved to eax, eax is returned

So, answer is 0xb0
