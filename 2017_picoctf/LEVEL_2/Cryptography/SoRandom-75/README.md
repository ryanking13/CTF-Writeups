## SoRandom - 75

### Description

We found [sorandom.py](./sorandom.py) running at shell2017.picoctf.com:23741. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?
Update (text only) 16:16 EST 1 Apr Running python 2 (same version as on the server)

### Hint

  - How random can computers be?

### Write up

The program is using `random` as a seed.

So if we also use `random` as a seed, the n-th random result must be the same.

```python
import random, string

num = "0123456789"
upp = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"

en = "BNZQ:1l36de9583w5516fv3b8691102224f3e"
res = ""
cnt = 0
for i in range(len(en)):
    c = en[i]
    if c.islower():
        for j in range(len(low)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0, 1)
            val = chr((ord(low[j])-ord('a')+random.randrange(0,26))%26 + ord('a'))
            if val == c:
                res += low[j]
                cnt += 1
                break
    elif c.isupper():
        for j in range(len(upp)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0, 1)
            val = chr((ord(upp[j])-ord('A')+random.randrange(0,26))%26 + ord('A'))
            if val == c:
                res += upp[j]
                cnt += 1
                break
    elif c.isdigit():
        for j in range(len(num)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0, 1)
            val = chr((ord(num[j])-ord('0')+random.randrange(0,10))%10 + ord('0'))
            if val == c:
                res += num[j]
                cnt += 1
                break
    else:
        res += c

print(res)
```

    $ python sorandom_solve.py
    FLAG:8a18af7233c1846ad6e1235654851b2d

> FLAG:8a18af7233c1846ad6e1235654851b2d
