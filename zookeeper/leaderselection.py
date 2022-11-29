from zookeeper import activepartitions
path = "Big Data\Brokers"
leader = []
# leader's index is the partition number
# and the value is the broker number

def init_leader(number_of_partitions):
    for i in range(number_of_partitions):
        leader[i]=i
    update()
def update():
    k=0
    for i in leader:
        if(i>0):
            print("partition: "+str(k)+" ------>broker: "+str(i)+"")
            activepartitions[i]=path+'part'+str(k)+'_'+str(i)
        k=k+1
def switch_leader(failedbroker):
    for i in leader: 
        if(i==failedbroker):
            nextbroker = (leader.index(i)+1)%3
            while(nextbroker<1):
                nextbroker =(nextbroker+1)%3
            leader[i]=nextbroker
    update()