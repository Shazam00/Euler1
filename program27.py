import time
tStart = time.time()
def isPrime(num):
    'checks if num is a prime number'
    if num < 0:
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

def primeFunc(n,a,b):
    'calculates result from a prime function'
    return n*n+a*n+b

def primeNum(a,b):
    'tests a prime function with consecutive number starting from 0'
    'breaks when the result is not a prime number'
    currVal = 0
    while currVal < 1000:
        if isPrime(primeFunc(currVal,a,b)) == False:
            break
        currVal+=1
    return currVal

data = []
for x in range(1999):
    data.append(x-999)
#print(data);
#print(primeNum(-79,1601))
#print(len(data))
maxA = 0
maxB = 0
maxPrime = 0
for a in range(1998):
    for b in range(1998):
        if primeNum(data[a],data[b]) > maxPrime:
            maxA = data[a]
            maxB = data[b]
            maxPrime = primeNum(maxA,maxB)
            print ("==> ",maxPrime," @  a=>",maxA," b=>",maxB)
print("a => ",maxA)
print("b => ",maxB)
print("Primes => ",maxPrime)
print ("Run Time = " , str(time.time() - tStart))

