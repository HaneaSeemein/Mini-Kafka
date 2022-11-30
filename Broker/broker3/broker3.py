import socket
from time import sleep
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    socket.sendto(b'hello', ('172.22.0.4', 9999))
    print('ALIVE 3')
    sleep(1)