import socket
import select

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_1.bind(('127.0.0.1', 9997))
socket_2.bind(('127.0.0.1', 9998))
socket_3.bind(('127.0.0.1', 9999))

poller = select.poll()
poller.register(socket_1, select.POLLIN)
poller.register(socket_2, select.POLLIN)
poller.register(socket_3, select.POLLIN)

while 1:
    evts = poller.poll(5000)
    for sock, evt in evts:
        if evt and select.POLLIN:
            if sock == socket_1.fileno():
                data1 = socket_1.recvfrom(4096)
                if data1:
                    print("Broker1 Alive")
                elif not data1:
                    print("Broker1 Dead")
            if sock == socket_2.fileno():
                data2 = socket_2.recvfrom(4096)
                if data2:
                    print("Broker2 Alive")
                elif not data2:
                    print("Broker2 Dead")
            if sock == socket_3.fileno():
                data3 = socket_3.recvfrom(4096)
                if data3:
                    print("Broker3 Alive")
                elif not data3:
                    print("Broker3 Dead")
            