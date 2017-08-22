import socket
import json

s = socket.socket.(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('longest-substr.eatpwnnosleep.com', 9000))

a = {
    'apikey' : '111fb6dbaafbac7ae805a98e0e87a3ebdccbf651a169efb60820eeb1520bebc6',
    'probid' : 'asdf',
    'sourcetype' : 'asdf',
    'code' : 'asdf',
}

s.send(json.dumps(a))
print (s.recv(102400))
