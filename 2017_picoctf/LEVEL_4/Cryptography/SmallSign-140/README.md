## SmallSign - 140

### Description

This service outputs a flag if you can forge an RSA signature!
nc shell2017.picoctf.com 10650
[smallsign.py](./smallsign.py)

### Hint

  - RSA encryption (and decryption) is multiplicative.

### Write up

```python
#!/usr/bin/python -u

from Crypto.PublicKey import RSA
import random
import signal

key = RSA.generate(2048)
flag = open("./flag").read()

print "You have 60 seconds to forge a signature! Go!"
# In 60 seconds, deliver a SIGALRM and terminate
signal.alarm(60)

print "N:", key.n
print "e:", key.e

while True:
    m = int(raw_input("Enter a number to sign (-1 to stop): "))
    if m == -1:
        break
    sig = key.sign(m, None)
    print "Signature:", str(sig[0])

challenge = random.randint(0, 2**32)
print "Challenge:", challenge
s = int(raw_input("Enter the signature of the challenge: "))
if key.verify(challenge, (s, None)):
    print "Congrats! Here is the flag:", flag
else:
    print "Nope, that's wrong!"
```

A random 2048 byte RSA object is generated.

We can send random number, and get signature of it.

Then, the `challenge` number is given, and we must give the signature of it.

We only have 60 seconds, so we can't make every numbers signature.


signature of message(number) m is calculate by the formula below.

> signature = m^d mod N

if m = m1 * m2 * m3 * ... * mi, we can manipulate the formula like this.

> signature = (m1^d mod N * m2^d mod N * ... mi^d mod N) * mod N

So, what we are going to do is pre-calculate signatures of some prime numbers. and represent `challenge` with multiple of prime numbers that we calculated.

```python
from pwn import *
import sys
import struct
import time

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
         197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
         ]

def primefac(num):
    l = []

    n = num
    for fac in primes:
        while n % fac == 0:
            l.append(fac)
            n /= fac

    if n != 1:
        return None

    return l

while True:
    signatures = []
    p = remote('shell2017.picoctf.com', 10650)

    s = time.time()

    p.recvuntil('N: ')
    N = int(p.recvline().strip())
    print('N:', N)

    for i in range(len(primes)):
        p.sendline(str(primes[i]))
        p.recvuntil('Signature: ')
        signatures.append(int(p.recvline().strip()))

    p.sendline('-1')
    p.recvuntil('Challenge: ')
    challenge = int(p.recvline().strip())
    print('challenge:', challenge)

    fac = primefac(challenge)

    e = time.time()

    print('time:', e-s)
    if not fac:
        p.close()
        continue

    print('primefac:', fac)

    ans = 1

    for num in fac:
        ans = (ans * signatures[primes.index(num)]) % N

    print('ans', ans)
    p.sendline(str(ans))
    p.interactive()

```

Since we only have 60 seconds, we can't calculate many primes either. So we rely on random iteration. So it takes quite a while. ( about an hour in my case) 

```
...
[+] Opening connection to shell2017.picoctf.com on port 10650: Done
('N:', 22221221066790191927079812189868633342807621551594052357667194990539752727578600637167829241188742615665150852297567966291364295705892811636068991463599072787532788449792220023903221106138141821642506366192956386896548638436349280936439100233891339712471522126154815123790227080130307266052221295385750248742703685446122067440228512337909582234573826876599379445538185563839971367239776975014017407361836516678214596796515481896798196934118974019218255598794035269990514377605225002418108728608514375507650554608011453117144093388994759235417371954807076333926169604462124297802631146700639000957956758791950438342469L)
('challenge:', 3168417909)
('time:', 32.34713697433472)
('primefac:', [3, 47, 271, 283, 293])
('ans', 19387008516590441033678654470654102719497425070371239137756809323214824338464476414083854556342714134679230439058194134244084881666170582171360182854832638348575019916026788494617204347791467369467187914939875068791228470808623631547894827992157801448064910023355577740768208003010801441273294398883011056689888719021317612455924028090185365392967756030180482128450269222274743094018563167771051817026552365644381638976175233390540930361678936998353147714080214935524884104014158871407760763604879816012096574999510682892670668196200717419685734105872555307274243604090800747649684351520164019688514528693521894538233L)
[*] Switching to interactive mode
Enter the signature of the challenge: Congrats! Here is the flag: 6298123dbccaf021eed3c55c79a806a3

```

> 6298123dbccaf021eed3c55c79a806a3
