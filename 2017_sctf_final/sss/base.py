import base64
import sys

name = sys.argv[1]

with open(name, 'r') as f:
    r = f.read()
    r = base64.b64encode(r.encode())
    print(r)