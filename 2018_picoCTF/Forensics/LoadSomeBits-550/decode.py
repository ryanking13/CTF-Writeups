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