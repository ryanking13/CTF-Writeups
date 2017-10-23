## HashChain - 90

### Description

We found a service hiding a flag! It seems to be using some kind of MD5 Hash Chain authentication to identify who is allowed to see the flag. Maybe there is a flaw you can exploit? [hcexample.py](./hcexample.py) has some example code on how to calculate iterations of the MD5 hash chain. Connect to it at shell2017.picoctf.com:57048!



### Hint

    $ nc localhost 57048

    ...

    Would you like to register(r) or get flag(f)?

    r/f?

    r
    Hello new user! Your ID is now 3701 and your assigned hashchain seed is b181eaa49f5924e16c772dcb718fcd0f
    Please validate your new ID by sending the hash before this one in your hashchain (it will hash to the one I give you):
    2c5e35e6d48e74283ec5d6647067d6d5

`b181eaa49f5924e16c772dcb718fcd0f` is MD5 hash value of `3701`, so the seed is MD5 value of the ID.

It wants the hash in our hashchain.

Let's make hashchain generator.

```python
# hasher.py
import md5

seed = "seed"
target = "target"

cnt = 0
while True:
	hash = md5.new(seed).hexdigest()

	if hash == target:
		print(seed)
		print(cnt)
		break

	else:
		seed = hash
		cnt+=1
```

If we set seed and target, the script returns the hash in hashchain just before the target.

    $ nc localhost 57048

    ...
    Would you like to register(r) or get flag(f)?

    r/f?

    f
    This flag only for user 4536
    Please authenticate as user 4536
    6d9d8cfaa21ab7ca3c9123c6aed6017a
    Next token?

---

set seed=4536, target=6d9d8cfaa21ab7ca3c9123c6aed6017a and run the script.

    $ python2 hasher.py
    2731ecdc9713ecf2ba08ce4f7d1f1b95
    65

---

    This flag only for user 4536
    Please authenticate as user 4536
    6d9d8cfaa21ab7ca3c9123c6aed6017a
    Next token?
    2731ecdc9713ecf2ba08ce4f7d1f1b95

    Hello user 4536! Here's the flag: 1897a39c3292c935fcfb849886e253d0

> 1897a39c3292c935fcfb849886e253d0
