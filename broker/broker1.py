import socket
from time import sleep
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    socket.sendto(b'hello', ('127.0.0.1', 9997))
    print('ALIVE 1')
    sleep(1)