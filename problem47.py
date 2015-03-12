import time
tStart = time.time()

def isPrime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))     # make sure n is a positive integer
    if n < 2:           # 0 and 1 are not primes
        return False
    if n == 2:          # 2 is the only even prime number
        return True
    if not n & 1:       # all other even numbers are not primes
        return False
    for x in range(3, int(n**0.5)+1, 2): # range starts with 3 and only needs to go up the squareroot of n
        if n % x == 0:                   # for all odd numbers
            return False
    return True

def getPrimeFactors(n):
    num = n
    queue = []
    check = False
    while isPrime(num) == False:
        divisor = 2
        while check == False:
            if isPrime(divisor):
                if num % divisor == 0:
                    num = int(num / divisor)
                    check = True
                    queue.append(divisor)
            divisor +=1;
        check = False
    queue.append(num)
    return queue

currNum = 600
fourSet = []
setCount = 0
count = 1
while count < 999999999:
    if len(list(set(getPrimeFactors(currNum)))) == 4:
        setCount +=1
        fourSet.append(currNum)
    else:
        setCount = 0
        fourSet = []
    if setCount == 4:
        break
    currNum+=1
    count = count+1

print (fourSet)
print ("Run Time = " , str(time.time() - tStart))



