import socket
import select
import time
path = "Big Data/Brokers"
leader = [0,0,0,0]
activepartitions=[0,0,0,0]
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

init_leader()
timer1=time.time()
timer2=time.time()
timer3=time.time()
def alive(socket):
    if(socket==1):
        # restart_timer1
        timer1=time.time()
        socket1_alive = True
    elif(socket==2):
        # restart_timer2
        timer2=time.time()
        socket2_alive = True
    elif(socket==3):
        # restart_timer3
        timer3=time.time()
        socket3_alive = True


while 1:
    evts = poller.poll(5000)
    if((timer1-time.time())>10):
        switch_leader(1)
        timer1=0
    if(timer2-time.time()>10):
        switch_leader(2)
        timer2=0
    if(timer3-time.time()>10):
        switch_leader(3)
        timer3=0
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
                    alive(2)
            if sock == socket_3.fileno():
                data3 = socket_3.recvfrom(4096)
                if data3:
                    print("Broker3 Alive")
                    alive(3)

            