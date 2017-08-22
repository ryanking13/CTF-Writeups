import socket
import json
import base64
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('sss.eatpwnnosleep.com', 18878))

a = {
    'apikey' : '111fb6dbaafbac7ae805a98e0e87a3ebdccbf651a169efb60820eeb1520bebc6',
}

print(json.dumps(a).encode())
s.send(json.dumps(a).encode())
print (s.recv(102400))
print (s.recv(102400))
print(s.recv(102400))

f1 = open('valenv.c', 'r').read()
f1 = base64.b64encode(f1.encode())

f2 = open('valenv.h', 'r').read()
f2 = base64.b64encode(f2.encode())

s.send(b'valenv.c\n')
print(s.recv(102400).decode())
s.send(f1 + b'\n')
print(s.recv(102400).decode())
print(s.recv(102400).decode())

s.send(b'valenv.h\n')
print(s.recv(102400).decode())
s.send(f2 + b'\n')

while True:
    recv = s.recv(102400)
    if len(recv) == 0:
        exit(0)

    print(recv.decode())
