import socket
import select
import time
path = "Big Data/Brokers"
leader = [0,0,0,0]
activepartitions=[0,0,0,0]

def update():
    k=0
    print(leader)
    for i in leader:
        if(i>0):
            print("partition: "+str(k)+" ------>broker: "+str(i)+"")
            activepartitions[k]=path+'/part'+str(k)+'_'+str(i)
        k=k+1
def init_leader():
    for i in range(4):
        leader[i]=i
    update()
def switch_leader(failedbroker):
    for i in range(len(leader)): 
        if(leader[i]==failedbroker):
            nextbroker = (leader[i]+1)%4
            while(leader[nextbroker]<1):
                nextbroker =(nextbroker+1)%4
            leader[i]=nextbroker
    update()
def alive(socket):
    if(socket==1):
        socket1_alive = True
    elif(socket==2):
        socket2_alive = True
    elif(socket==3):
        socket3_alive = True
def dead():
    time.sleep(5)
    socket1_alive = False
    socket2_alive = False
    socket3_alive = False

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
init_leader()
while 1:
    evts = poller.poll(5000)
    dead()
    for sock, evt in evts:
        if evt and select.POLLIN:
            if sock == socket_1.fileno():
                data1 = socket_1.recvfrom(4096)
                if data1:
                    print("Broker1 Alive")
                    alive(1)

            if sock == socket_2.fileno():
                data2 = socket_2.recvfrom(4096)
                if data2:
                    print("Broker2 Alive")

            if sock == socket_3.fileno():
                data3 = socket_3.recvfrom(4096)
                if data3:
                    print("Broker3 Alive")

            