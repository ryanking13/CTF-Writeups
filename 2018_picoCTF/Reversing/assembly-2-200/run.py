
_a = 0
_b = 0

def asm2(a, b):
    global _a
    global _b

    _a = a
    _b = b

    while _a <= 0x8f90:
        _b += 0x1
        _a += 0x8f

    return _b


print(hex(asm2(0x6, 0x28)))