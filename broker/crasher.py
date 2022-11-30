def main():
    kill = [0,-1,-1,-1]
    tokill1 = int(input("Enter the broker to kill"))
    tokill2 = int(input("Enter the another broker to kill(if any)"))
    t1 = int(input("Enter the timeout for the first kill"))
    t2 = int(input("Enter the timeout for the second kill"))
    kill[tokill1]=t1
    kill[tokill2]=t2
    return kill
