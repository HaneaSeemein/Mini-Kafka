import socket
import select
from datetime import datetime
path = "Big Data/Brokers"
# change this path to whatever decided
leader = [0, 0, 0, 0]
activepartitions = [0, 0, 0, 0]
# leader's index is the partition number
# and the value is the broker number


def update():
    k = 0
    print(leader)
    for i in leader:
        if (i > 0):
            print("partition: "+str(k)+" ------>broker: "+str(i)+"")
            activepartitions[k] = path+'/part'+str(k)+'_'+str(i)
        k = k+1


def init_leader():
    for i in range(4):
        leader[i] = i
    update()


def switch_leader(failedbroker):
    for i in range(len(leader)):
        if (leader[i] == failedbroker):
            nextbroker = (leader[i]+1) % 4
            while (leader[nextbroker] < 1):
                nextbroker = (nextbroker+1) % 4
            leader[i] = nextbroker
    update()


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


iterations = 0
count1 = 0
count2 = 0
count3 = 0

alive1 = 1
alive2 = 1
alive3 = 1

now = datetime.now()
start_time = now.second
init_leader()
while 1:
    now1 = datetime.now()
    current_time = now1.second
    if abs(current_time-start_time) >= 10:
        start_time = current_time
        if alive1 == 0:
            print("run leader selection for broker1")
            # switch_leader(1)
        if alive2 == 0:
            print("run leader selection for broker2")
            # switch_leader(2)
        if alive3 == 0:
            print("run leader selection for broker3")
            # switch_leader(3)

    evts = poller.poll(20)
    alive1 = 0
    alive2 = 0
    alive3 = 0
    for sock, evt in evts:
        print(iterations)
        iterations = iterations + 1
        if evt and select.POLLIN:
            if sock == socket_1.fileno():
                data1 = socket_1.recv(4096)
                print(sock)
                count1 = 1
                alive1 = 1
                if data1:
                    print("Broker1 Alive")
                    now_1 = datetime.now()
                    start_time = now_1.second
            elif sock == socket_2.fileno():
                data2 = socket_2.recv(4096)
                print(sock)
                count2 = 1
                alive2 = 1
                if data2:
                    now_2 = datetime.now()
                    start_time = now_2.second
                    print("Broker2 Alive")
            elif sock == socket_3.fileno():
                data3 = socket_3.recv(4096)
                print(sock)
                count3 = 1
                alive3 = 1
                if data3:
                    now_3 = datetime.now()
                    start_time = now_3.second
                    print("Broker3 Alive")
        if iterations % 4 == 0:
            if count1 != 1:
                print("BROKER 1 DEAD")
                alive1 = 0
            else:
                count1 = 0
            if count2 != 1:
                print("BROKER 2 DEAD")
                alive2 = 0
            else:
                count2 = 0
            if count3 != 1:
                print("BROKER 3 DEAD")
                alive3 = 0
            else:
                count3 = 0
            iterations = 0
        else:
            print(iterations)
