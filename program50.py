import time
tStart = time.time()

def isPrime(num):
    'checks if num is a prime number'
    if num < 0:
        return False
    if num == 1:
        return False
    result = True
    currValue = 2
    maxValue = num/2
    while currValue <= maxValue:
        if num % currValue == 0:
            result = False
            break
        currValue+=1
    return result

def isConsecutiveSum(num,data):
    target = num
    total = 0
    #data.sort()
    currMax = []
    for x in range(len(data)-1):
        if data[x] >= num:
            break
        sumList = []
        total = 0
        for y in range(len(data)):
            if total < target:
                sumList.append(data[y+x])
                total+=data[y+x]
                if total == target:
                    if len(currMax) < len(sumList):
                        currMax = sumList
                        break
            else:
                break
    return currMax
store = []
MaxNum = 0
MaxChain = []
done = 0

filename = "primes.txt"
f = open(filename,"r")
text = f.readline() 
data = ''
while len(text) != 0:
    data = data + text
    text = f.readline() 
primeList = data.split(',')
print(len(primeList))

a = 0
b = len(primeList) -1
while a <= b:
    primeList[a] =  primeList[a].rstrip()
    primeList[a] = int(primeList[a])
    a+=1


print(primeList[len(primeList)-1])
count = 0
print (len(primeList))
rev = []
rev.extend(primeList)
rev.reverse()
print(primeList[len(primeList)-1])

for x in rev:
    tempChain = isConsecutiveSum(x,primeList)
    if len(tempChain) > len(MaxChain):
        MaxNum = x
        MaxChain = tempChain
    count+=1
    if count % 100 == 0:
        print (round(count/len(primeList)*100,2), " % complete --- current number: ", x, "   current Max: ",MaxNum, "   Chain Length: ",len(MaxChain),"   Time: ", str(time.time() - tStart))

#print (isConsecutiveSum(997651,primeList))

print ("Max Number:", MaxNum)
print ("Max Chain Sum:", MaxChain)    
print ("Run Time = " , str(time.time() - tStart))

#30  % complete --- current number:  290001    current Max:  287137   Time:  1769.829999923706
#31  % complete --- current number:  300001    current Max:  287137   Time:  1884.7039999961853
#32  % complete --- current number:  310001    current Max:  303691   Time:  2005.7430000305176
#33  % complete --- current number:  320001    current Max:  318557   Time:  2130.28200006485


#0.13  % complete --- current number:  998551    current Max:  998857    Chain Length:  509    Time:  34.128000020980835
#0.25  % complete --- current number:  997201    current Max:  997651    Chain Length:  543    Time:  68.1930000782013

