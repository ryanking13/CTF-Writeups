import pyqrcode

def gen_rand_str(n):
    with open('/dev/urandom', 'r') as f:
        data = b64e(f.read(n))[:n]

    return data

def gen_qrcode(n=DEFAULT_LEN):
    data = gen_rand_str(n)
    qrdata = pyqrcode.create(data, version=VERSION)

    return qrdata.code, data