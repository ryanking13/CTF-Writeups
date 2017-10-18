## Raw2Hex - 20

### Description

This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it!

CLI yourself to /problems/963285fb64e4c5f7a31b5a601c704f99 and turn that Raw2Hex!

### Hint

  - Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

### Write up

    $ ./raw2hex
    The flag is:㚧ª~Y?މªB>¤

The flag is given in raw bytes.

```python
a = raw_input()
b = 'The flag is:'
a = a[len(b):]

print a.encode('hex')
```

Write a simple python script that decodes raw bytes to hex value. We can use /tmp/ folder for writing a script.

    $ ./raw2hex | python /tmp/decode.py
    e519e7aa7e593fde891bd24aaa423ea4


> e519e7aa7e593fde891bd24aaa423ea4
