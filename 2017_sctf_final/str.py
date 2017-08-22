import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('longest-substr.eatpwnnosleep.com', 9000))

code = open("str.cpp", "r").read()

a = {
    'apikey': '111fb6dbaafbac7ae805a98e0e87a3ebdccbf651a169efb60820eeb1520bebc6',
    'probid': 'longest-substr',
    'sourcetype': 'cpp',
    'code': code,
}

# print(code)
s.send(json.dumps(a).encode())
print(s.recv(102400))