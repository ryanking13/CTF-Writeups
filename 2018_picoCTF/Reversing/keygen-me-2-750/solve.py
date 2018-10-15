from z3 import *

def decode(val):
    if val < 10:
        return chr(ord('0') + val)
    else:
        return chr(ord('A') - 10 + val)

key = [Int('x%d' % i) for i in range(16)]

s = Solver()
for i in range(16):
    s.add(key[i] >= 0)
    s.add(key[i] <= 35)

# const 01-12
s.add( (key[0] + key[1]) % 36 == 14 )
s.add( (key[2] + key[3]) % 36 == 24 )
s.add( (key[2] - key[0]) % 36 == 6 )
s.add( (key[1] + key[3] + key[5]) % 36 == 4 )
s.add( (key[2] + key[4] + key[6]) % 36 == 13 )
s.add( (key[3] + key[4] + key[5]) % 36 == 22 )
s.add( (key[6] + key[8] + key[10]) % 36 == 31 )
s.add( (key[1] + key[4] + key[7]) % 36 == 7)
s.add( (key[9] + key[12] + key[15]) % 36 == 20)
s.add( (key[13] + key[14] + key[15]) % 36 == 12)
s.add( (key[8] + key[9] + key[10]) % 36 == 27)
s.add( (key[7] + key[12] + key[13]) % 36 == 23)

s.check()
model = s.model()
res = [ model.eval(key[i]).as_long() for i in range(16) ]
print(''.join([decode(int(r)) for r in res]))