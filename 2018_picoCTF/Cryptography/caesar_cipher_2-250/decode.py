c = '^WQ]1B4iQ/SaO@M1W>V3`AMXcABMO@3\\BMa3QC`3k'

def decode(rot):
    a = []
    for cc in c:
        a.append(chr(ord(cc) + rot))

    print(rot, ''.join(a))

for i in range(-30, 30):
    decode(i)