import os
import sys
path = "C:\Users\haniy\Desktop\Big Data\Brokers\brokerx"
active = True

leader = []
# leader's index is the partition number
# and the value is the broker number
L_partitions=[]

def init_leader(number_of_partitions):
    for i in range(number_of_partitions):
        leader[i]=i
def update():
    k=0
    for i in leader:
        if(i>0):
            L_partitions[i]=path+'part'+str(k)+'_'+str(i)
        k=k+1
def switch_leader(failedbroker):
    for i in leader: 
        CBleader = (leader.index(i)+1)%3
        if(i==failedbroker):
            nextbroker = (leader.index(i)+1)%3
            while(nextbroker<1):
                nextbroker =(nextbroker+1)%3
            leader[i]=nextbroker

