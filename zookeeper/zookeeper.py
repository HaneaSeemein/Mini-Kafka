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
import socket
import select
from datetime import datetime

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_1.bind(('127.0.0.1', 9997))
socket_2.bind(('127.0.0.1', 9998))
socket_3.bind(('127.0.0.1', 9999))

path = "/Users/sailu/Documents/BD/zookeeper"

leader = [0,0,0,0]
activepartitions=[0,0,0,0]

poller = select.poll()
poller.register(socket_1, select.POLLIN)
poller.register(socket_2, select.POLLIN)
poller.register(socket_3, select.POLLIN)




iterations = 0
count1 = 0
count2 = 0
count3 = 0

alive1 = 0
alive2 = 0
alive3 = 0

leader_ran1 = 0
leader_ran2 = 0
leader_ran3 = 0

now = datetime.now()
start_time = now.second
init_leader()
while 1:
    #every 60 seconds check the health of all brokers
    #run leader selection for dead brokers
    now1 = datetime.now()
    current_time = now1.second
    # #print("diff in time(sec)",current_time-start_time)
    if abs(current_time-start_time)>=10:
        start_time = current_time
        #print("alive1: ",alive1)
        #print("alive2: ",alive2)
        #print("alive3: ",alive3)
        if alive1 == 0:
            print("run leader selection for broker1")
            switch_leader(1)
        if alive2 == 0:
            print("run leader selection for broker2")
            switch_leader(2)
        if alive3 == 0:
            print("run leader selection for broker3")
            switch_leader(3)
        
    evts = poller.poll(20)
    # alive1 = 0
    # alive2 = 0
    # alive3 = 0
    #print("check event")
    for sock, evt in evts:
        iterations = iterations + 1
        #print("before socket poll: ",iterations)
        if evt and select.POLLIN:
            #print("iterations at beggining: ",iterations)
            if sock==socket_1.fileno():
                data1 = socket_1.recv(4096)
                count1 = 1
                alive1 = 1
                #print("count in broker1",count)
                #print("count in broker1",iterations)
                if data1:
                    print("Broker1 Alive")
            elif sock == socket_2.fileno():
                data2 = socket_2.recv(4096)
                count2 = 1
                alive2 = 1
                #print("count in broker2",count)
                #print("count in broker2",iterations)
                if data2:
                    print("Broker2 Alive")
            elif sock == socket_3.fileno():
                data3 = socket_3.recv(4096)
                count3 = 1
                alive3 = 1
                #print("count in broker3",count)
                #print("count in broker3",iterations)
                if data3:
                    print("Broker3 Alive")
        if iterations%3==0:
            if count1!=1:
                print("BROKER 1 DEAD")
                alive1 = 0
            else:
                count1=0
            if count2!=1:
                print("BROKER 2 DEAD")
                alive2 = 0
            else:
                count2=0
            if count3!=1:
                print("BROKER 3 DEAD")
                alive3 = 0
            else:
                count3=0
            iterations = 0