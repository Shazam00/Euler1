import time
tStart = time.time()


def printChain(num):
    chainList = []
    numList = list(str(num))
    currNum = num
    while True :
        if currNum in chainList:
            break
        chainList.append(currNum)
        numList = list(str(currNum))
        currNum = 0
        for x in numList:
            currNum += int(x)**2
    #print(chainList)
    return chainList

count = 1
chain = []
done = 0
for x in range(10000000):
    if 89 in printChain(x+1):
        count+=1
    if x % 100000 ==0 :
        done+=1
        print(round(done,2),"%  --","  Current number: ", x ,"count: ", count," Time: ",str(time.time() - tStart))
print (count-1)
print ("Run Time = " , str(time.time() - tStart))

#8581146
