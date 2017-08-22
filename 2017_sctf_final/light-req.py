import socket
import json
import struct
import time
import random

color = {
    'R' : 0,
    'G' : 1,
    'B' : 2,
}

x = [-1, 1, 0, 0]
y = [0, 0, 1, -1]

apikey = b'111fb6dbaafbac7ae805a98e0e87a3ebdccbf651a169efb60820eeb1520bebc6\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('3-lights.eatpwnnosleep.com', 22341))

print(s.recv(102400).decode())
s.send(apikey)
print(s.recv(102400).decode())

print(s.recv(102400).decode())

prob = []

recv = s.recv(102400).decode().strip('\n').split()
for i in range(len(recv)):
    r = []
    for j in range(len(recv[i])):
        r.append(color[recv[i][j]])

    if r:
        prob.append(r)

recv = s.recv(102400).decode().strip('\n').split()
for i in range(len(recv)):
    if recv[i] == 'answer:':
        break

    r = []
    for j in range(len(recv[i])):
        r.append(color[recv[i][j]])

    if r:
        prob.append(r)

# print(prob)

dp = []
qrcode = []
for i in range(len(prob)):
    dp.append([0 for j in range(len(prob[0]))])
    qrcode.append([0 for j in range(len(prob[0]))])

# print(dp)

for i in range(1, len(prob)):

    for j in range(len(prob[0])):
        diff = abs(prob[i-1][j] - dp[i-1][j])
        if diff == 0:
            qrcode[i][j] = 0
        elif diff == 1:
            qrcode[i][j] = 2
            flood(dp, i, j, qrcode[i][j])
        elif diff == 2:
            qrcode[i][j] = 1
            flood(dp, i, j, qrcode[i][j])


def flood(dp, i, j, val):
    dp[i][j] += val
    dp[i][j] %= 3
    for d in range(4):
        xx = i + x[d]
        yy = j + y[d]

        if xx > -1 and xx < len(dp[0]) and yy > -1 and yy < len(dp):
            dp[xx][yy] += 3 - val
            dp[xx][yy] %= 3
