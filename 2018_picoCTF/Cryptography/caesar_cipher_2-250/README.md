## caesar cipher 2 - 250

### Description

> Can you help us decrypt this message? We believe it is a form of a caesar cipher. You can find the ciphertext in /problems/caesar-cipher-2_0_372a62ea0204b948793a2b1b3aeacaaa on the shell server.

### Write up

caesar cipher, but not limited in alphabet range.

Since we don't know the key, let's brute force it.

```
c = '^WQ]1B4iQ/SaO@M1W>V3`AMXcABMO@3\\BMa3QC`3k'

def decode(rot):
    a = []
    for cc in c:
        a.append(chr(ord(cc) + rot))

    print(rot, ''.join(a))

for i in range(-30, 30):
    decode(i)
```

```
...
17 ohbnBSEzb@dr`Q^BhOgDqR^itRS^`QDmS^rDbTqD|
18 picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
19 qjdpDUG|dBftbS`DjQiFsT`kvTU`bSFoU`tFdVsF~
...
```
