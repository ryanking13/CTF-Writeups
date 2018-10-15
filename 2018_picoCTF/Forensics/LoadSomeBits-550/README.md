## LoadSomeBits - 550

### Description

> Can you find the flag encoded inside this image? You can also find the file in /problems/loadsomebits_3_8933ebe9085168b1e0bbb07884c2231f on the shell server.

### Write up

By opening image file with hex viewer, there are bunch of 0 and 1.

```
01 00 01 00 00 01 00 01 01 00 00 00 01 01 00 01 01 00 01 01 01 01 00 01 00 00 00 00 01 01 00 01 00 01 00 01 00 00 00 01 00 00 00 01 01 00 00 01 01 01 01 00 01 01 00 01 01 01 00 00 01 01 00 01 01 01 00 01 00 00 00 00 01 01 00 00 00 00 00 01 01 01 00 00 01 00 00 00 01 01 00 00 01 01 00 01 01 00 00 01 00 00 00 01 00 01 01 01 01 01 00 01 01 00 01 00 00 01 00 01 00 00 01 01 01 00 00 01 00 01 01 01 01 01 00 01 01 01 00 01 00 00 00 01 00 00 01 00 00 00 00 00 01 01 00 00 01 01 00 01 00 01 01 01 01 01 00 01 01 00 01 01 00 00 00 00 01 01 00 00 01 01 00 00 01 01 00 01 00 00 00 00 01 01 00 01 00 01 00 01 01 01 00 01 00 00 00 01 00 01 01 01 01 01 00 01 01 01 00 00 01 01 00 00
```

which means it can be an ASCII code.

picoCTF in ASCII is {01110000 01101001 01100011 01101111 01000011 01010100 01000110},

which can be found from offset 0x36.

```
f = open('pico2018-special-logo.bmp', 'rb')
data = f.read()
f.close()

data = data[0x36:]
l = len(data)

for i in range(0, l, 8):
    d = data[i:i+8]
    binary = ''.join([str(s) for s in d])

    if binary == '00000000':
        break

    print(chr(int(binary, 2)), end='')
``` 