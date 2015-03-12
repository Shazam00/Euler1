import time
tStart = time.time()

def isPandigital(num,length):
    a = list(set(list(str(num))));
    a.sort()
    if len(list(str(num))) > int(a[len(a)-1]):
        return False
    if len(list(str(num))) != length:
        return False
    count = 1
    for n in a:
        if int(n) != count:
            return False
        else:
            count+=1
    return True

def listConcate(l):
    result = []
    s = ''
    for x in l:
        s = s + str(x)
    result.append(int(s))
    return result

currNum = 1
multiplier = 1
product = 0
check = 0
currMax = 0
for x in range(200000):
    multiplier = 1
    currNum = x+1
    currList = [currNum]
    while len(str(currList)) < 9:
        if multiplier !=1:
            currList.append(currNum*multiplier)
        currList = listConcate(currList)
        multiplier+=1
    if isPandigital(currList[0],9):
        if currList[0] > currMax:
            currMax = currList[0]
        print(currNum, " -> ", currList[0])

print ("largest number: ", currMax)
print ("Run Time = " , str(time.time() - tStart))

# 9327  ->  932718654
# largest number:  932718654