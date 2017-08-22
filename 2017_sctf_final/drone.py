import socket
import json
import struct
import time
import random
import zlib
import binascii
import struct

def switch_endian(s):
    s_le = ''
    for i in range(0, len(s), 2):
        s_le = s[i:i+2] + s_le

    return s_le


def rev(packet):

    byte_packet = bytearray.fromhex(packet)
    byte_packet = bytes(byte_packet)

    value = int.from_bytes(byte_packet, byteorder='little')
    value = int('{:08b}'.format(value)[::-1], 2)

    return hex(value)[2:]

def getcrc32(packet):
    byte_packet = bytearray.fromhex(packet)
    byte_packet = bytes(byte_packet)

    crc = binascii.crc32(byte_packet)
    crc = (crc & 0xFFFFFFFF)
    # crc = int('{:08b}'.format(crc)[::-1], 2)
    s = str("%08x" % crc)
    s_le = switch_endian(s)
    return s_le

# def getcrc32(packet):
#
#     byte_packet = packet.encode()
#     crc = zlib.crc32(byte_packet)
#
#     crc = crc & 0xFFFFFFFF
#     return str("%08x" % crc)

def random_header():
    chrs = '1234567890'
    l = 1

    c = ''
    for i in range(l):
        c += chrs[random.randint(0, len(chrs)-1)]

    return c

def random_text(l=4):
    # chrs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz1234567890 '
    chrs = '0123456789abcdef'
    n = len(chrs)

    # text_len = random.randint(8, 20)
    text_len = random.randint(l, l)

    # prefix = ('%02x' % (6 + text_len/2)) + '000000'
    prefix = '0c000000'
    suffix = '0000'
    c = ''
    for i in range(text_len):
        c += chrs[random.randint(0, n-1)]

    # c = header + c[len(header):]
    return prefix + c + suffix

def decode(text):
    c = ''
    i = 0
    while i < len(text)-2:

        if text[i] == '\n':
            c += '\n'
            i += 1
            continue

        try:
            c += chr(int(text[i:i+2], 16))
        except:
            return text

        i += 2

    return c

    for i in range(0, len(text)-2, 2):
        try:
            c += chr(int(text[i:i+2], 16))
        except:
            return text
    return c


def code(text):
    c = ''
    for i in range(0, len(text)):
        if text[i] == '\n':
            c += '\n'
        else:
            c += hex(ord(text[i]))[2:]

    return c

a = {
    'apikey': '111fb6dbaafbac7ae805a98e0e87a3ebdccbf651a169efb60820eeb1520bebc6',
}
print(json.dumps(a).encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('52.79.123.129', 31234))
s.send(json.dumps(a).encode())
print(s.recv(102400))
recv = s.recv(102400)
recv = recv.decode()
print(decode(recv))
print('-------------')

t = random_text()
t = t + getcrc32(t)
# fucking little endian!
print(t)
#print(code(t))
#s.send(code(t+'\n').enwcode())
s.send((t + '\n').encode())
recv = s.recv(102400)
recv = recv.decode()

err = '[-] That is not my UID, my uid is '
print(decode(recv))
if decode(recv).startswith(err):

    uid = int(decode(recv)[len(err):].strip())
    uid = switch_endian(hex(uid)[2:])

    t = '0c000000' + uid + '0000'
    t = t + getcrc32(t)

    print(t)
    s.send((t + '\n').encode())
    recv = s.recv(102400)
    recv = recv.decode()

    print('recv', decode(recv))
    if decode(recv).startswith('[-] Unknown command'):

        # cmd = 4626 # description page
        # cmd = 12336 # current loc/alt -> must move drone to base
        # cmd = 16448 # rotor control is allowed only on calibrated mode
        # cmd = 26213 # change altitude of drone
        # cmd = 30840 # set waypoint (must be armed first)
        cmd = 65278
        while True:
            # time.sleep(0.5)
            cmd_fmt = '%04x' % cmd

            t = '0e000000' + uid + switch_endian(cmd_fmt) + '0200'
            t = t + getcrc32(t)

            print(t)
            s.send((t + '\n').encode())
            recv = s.recv(102400)
            recv = recv.decode()
            print('recv', decode(recv))

            if decode(recv).startswith('[-] Unknown command'):
                cmd += 1
            else:

                recv = s.recv(102400)
                recv = recv.decode()
                break


print('---------------------------------')

decoded = decode(recv)
print(decoded)

# ------------- calibrate

# t = '0e000000' + uid + switch_endian(cmd_fmt) + '0200'
# t = t + getcrc32(t)
#
# print(t)
# s.send((t + '\n').encode())
# recv = s.recv(102400)
# recv = recv.decode()
# print('recv', decode(recv))
#
recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

print('------------calibrate done-----------')
# ------------------------ rotor

print('------------rotor 0000--------------')

for motor_id in [17,18,19,20]:

    rotor = 16448
    rotor_fm = '%04x' % rotor

    t = '0f000000' + uid + switch_endian(rotor_fm) + ('%02x' % motor_id) + '0000'
    t = t + getcrc32(t)

    s.send((t + '\n').encode())

    recv = s.recv(102400)
    recv = recv.decode()
    print('recv', decode(recv))

for motor_id in [17,18,19,20]:

    rotor = 16448
    rotor_fm = '%04x' % rotor

    t = '0f000000' + uid + switch_endian(rotor_fm) + ('%02x' % motor_id) + 'ffff'
    t = t + getcrc32(t)

    s.send((t + '\n').encode())

    recv = s.recv(102400)
    recv = recv.decode()
    print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

print('-------- arm --------')

atti = 65278
atti_fm = '%04x' % atti

t = '0e000000' + uid + switch_endian(atti_fm) + '0100'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

print('---------- fly! -----------')

atti = 26214
atti_fm = '%04x' % atti

t = '10000000' + uid + switch_endian(atti_fm) + '99994944'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

print('------------')


atti = 12336
atti_fm = '%04x' % atti

t = '0c000000' + uid + switch_endian(atti_fm)
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

print('---------------------')

time.sleep(5)

atti = 30840
atti_fm = '%04x' % atti

t = '14000000' + uid + switch_endian(atti_fm) + '0000004000004842'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

time.sleep(12)

atti = 30840
atti_fm = '%04x' % atti

t = '14000000' + uid + switch_endian(atti_fm) + '0000004000008041'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

time.sleep(12)

atti = 30840
atti_fm = '%04x' % atti

t = '14000000' + uid + switch_endian(atti_fm) + '0000c84100008041'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

time.sleep(12)

atti = 26214
atti_fm = '%04x' % atti

t = '10000000' + uid + switch_endian(atti_fm) + '00000000'
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

time.sleep(12)

print('------------')


atti = 12336
atti_fm = '%04x' % atti

t = '0c000000' + uid + switch_endian(atti_fm)
t = t + getcrc32(t)

s.send((t + '\n').encode())

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))

recv = s.recv(102400)
recv = recv.decode()
print('recv', decode(recv))


# t = '0c000000' + uid + switch_endian(cmd_fmt)
# t = t + getcrc32(t)
#
# print(t)
# s.send((t + '\n').encode())
# recv = s.recv(102400)
# recv = recv.decode()
# print('recv', decode(recv))

# [+] actions: ['help', 'print_location', 'control_rotor', 'change_altitude', 'moveto', 'change_mode']
# [+] this drone is supported by the SuperSafe company
# [+] to fly, calibration should be preceded


# [+] altitude: 0.000000m
# [+] location (x: 20.000000, y: 50.000000)
# [+] You need to move the drone to the base
# [+] map boundary: ((1, 1), (80, 54))

# [-] rotor control can be only allowed in calibrated mode.
# [-] otherwise, the drone will be crashed if you are not an expert

# [+] change altitude of drone
# [-] Drone should be armed first

# recv [+] set the waypoint of drone
# [-] Drone should be armed first

# SCTF{WoW!NowYouCanHackUnknownProtocol!}