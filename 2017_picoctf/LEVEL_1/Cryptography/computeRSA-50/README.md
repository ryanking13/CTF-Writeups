## computeRSA - 50

### Description

RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?

### Hint

  - decrypted = (encrypted) ^ d mod N

### Write up

Write a python [script](./decript.py).

```python
e = 150815
d = 1941
N = 435979

dec = 1
for i in range(d):
	dec = dec * e
	dec %= N

print(dec)
```

> 133337
