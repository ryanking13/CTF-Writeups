## quackme - 200

### Description

> Can you deal with the Duck Web? Get us the flag from this program. You can also find the program in /problems/quackme_2_45804bbb593f90c3b4cefabe60c1c4e2.

### Write up

Let's analyze `do_magic` function.

```
   0x08048648 <+6>: call   0x80485db <read_input>
```

It first reads user input,

```
   0x080486bd <+123>:   mov    eax,DWORD PTR [ebp-0x18]
   0x080486c0 <+126>:   add    eax,0x8048858 (sekrutBuffer)
```

then it reads data from something named `sekrutBuffer`


```
   0x080486d3 <+145>:   xor    eax,ecx
```

XOR user input and sekurBuffer byte by byte

```
   0x080486d5 <+147>:   mov    BYTE PTR [ebp-0x1d],al
   0x080486d8 <+150>:   mov    edx,DWORD PTR ds:0x804a038 (greetingMessage)
   0x080486de <+156>:   mov    eax,DWORD PTR [ebp-0x18]
   0x080486e1 <+159>:   add    eax,edx
   0x080486e3 <+161>:   movzx  eax,BYTE PTR [eax]
   0x080486e6 <+164>:   cmp    al,BYTE PTR [ebp-0x1d]
```

compares it with `greetingMessage` string, which is "You have now entered the Duck Web, and you're in for a honkin' good time."

If all comparison is successful, it prints "you are the winner!".

So, let's generate input which makes us the winner.

```
key = "You have now entered the Duck Web, and you're in for a honkin' good time."
enc = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x56\x47\x57\x50\x16\x4d\x51\x51\x5d"

for i in range(len(enc)):

    ok = ord(key[i])
    oe = ord(enc[i])

    print(chr(ok ^ oe), end='')
```

```
picoCTF{qu4ckm3_35246994}
```