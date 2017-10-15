import hashlib

alnum = '1234567890'


def try_crack(prefix):
    for al in alnum:
        candidate = prefix + al

        h = hashlib.md5(candidate.encode('utf-8')).hexdigest()

        if h.startswith('0e'):
            try:
                int(h[2:])
                print(candidate)
                exit()
            except:
                continue


pre = '0e'
num = 0

while True:
    try_crack('%s%d' % (pre, num))
    num += 1

# 0e1137126905
# 0e215962017