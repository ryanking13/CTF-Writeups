import random, string

num = "0123456789"
upp = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
low = "abcdefgijklmnopqrstuvwxyz"

en = "BNZQ:2m8807395d9os2156v70qu84sy1w2i6e"
res = ""
cnt = 0
for i in range(len(en)):
    c = en[i]
    if c.islower():
        for j in range(len(low)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0,1)
            val = chr((ord(low[j])-ord('a')+random.randrange(0,26))%26 + ord('a'))
            if val == c:
                res += low[j]
                cnt += 1
                break
    elif c.isupper():
        for j in range(len(upp)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0,1)
            val = chr((ord(upp[j])-ord('A')+random.randrange(0,26))%26 + ord('A'))
            if val == c:
                res += upp[j]
                cnt += 1
                break
    elif c.isdigit():
        for j in range(len(num)):
            random.seed("random")
            for k in range(cnt):
                random.randrange(0,1)
            val = chr((ord(num[j])-ord('0')+random.randrange(0,10))%10 + ord('0'))
            if val == c:
                res += num[j]
                cnt += 1
                break
    else:
        res += c

print(res)
