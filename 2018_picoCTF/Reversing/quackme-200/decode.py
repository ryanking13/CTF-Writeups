key = "You have now entered the Duck Web, and you're in for a honkin' good time."
enc = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x56\x47\x57\x50\x16\x4d\x51\x51\x5d"

for i in range(len(enc)):

    ok = ord(key[i])
    oe = ord(enc[i])

    print(chr(ok ^ oe), end='')