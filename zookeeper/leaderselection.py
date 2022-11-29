# from zookeeper import activepartitions
path = "Big Data/Brokers"
leader = [0,0,0,0]
activepartitions=[0,0,0,0]
# leader's index is the partition number
# and the value is the broker number

def init_leader():
    for i in range(4):
        leader[i]=i
    update()
def update():
    k=0
    print(leader)
    for i in leader:
        if(i>0):
            print("partition: "+str(k)+" ------>broker: "+str(i)+"")
            activepartitions[k]=path+'/part'+str(k)+'_'+str(i)
        k=k+1
def switch_leader(failedbroker):
    for i in range(len(leader)): 
        if(leader[i]==failedbroker):
            nextbroker = (leader[i]+1)%4
            while(leader[nextbroker]<1):
                nextbroker =(nextbroker+1)%4
            leader[i]=nextbroker
    update()
def process():
    print("Connected and initialised")
    init_leader()
    # print(activepartitions)
    failure = int(input("Enter the failed broker--"))
    switch_leader(failure)
    secfailure = int(input("Enter the second failed broker--"))
    switch_leader(secfailure)
process()
print(activepartitions)