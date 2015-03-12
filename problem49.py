import time
import itertools
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
#print(isPrime(1487))
test = list(itertools.permutations([1,4,8,7]))
#print(test)
count = 0
currNum = 1000
data = []
solution = []
while currNum < 10000:
    if isPrime(currNum):
        data.append(currNum)
        count+=1
    currNum+=1
numPrime = 0
#print(data[0])

for a in data: # for each prime number between 1000 to 9999
    NumberPermutations = []
    for b in str(a):     # for each digit in a prime number
        NumberPermutations.append(int(b))     # gets the prime in a list form 
    #print (NumberPermutations)
    NumberPermutations = list(itertools.permutations(NumberPermutations))   # gets all the permutations in list form
    numPrime = 0
    tempList = []
    for c in NumberPermutations: # for each [x,x,x,x] in list of permutations of the prime number
        testVal = ""
        testInt = 0
        for d in range(4):
            testVal = testVal + str(c[d]) 
        testInt = int(testVal)
        if testInt == 3330 + a or  testInt == 2*3330 + a:
            if isPrime(testInt) == True:
                numPrime +=1
                tempList.append(testInt)
    if numPrime > 2:
        print (a)
        solution.append(tempList)


print (len(solution))
print (solution)

print ("Run Time = " , str(time.time() - tStart))

#2969+6299+9629




