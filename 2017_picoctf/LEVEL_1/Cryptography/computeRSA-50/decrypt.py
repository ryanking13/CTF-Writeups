e = 150815
d = 1941
N = 435979

dec = 1
for i in range(d):
	dec = dec * e
	dec %= N

print(dec)

print(pow(e, d, N))