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


compositeNumbers = []
primeList = []
for a in range(10000):
    if isPrime(a+1) == False:
        if (a+1) % 2 != 0:
            compositeNumbers.append(a+1)
    else:
        primeList.append(a+1)
for b in compositeNumbers:
    # composite number  = prime + 2* num^2
    found = False
    for c in primeList: # for each prime number
        if c > b:
            break
        num = 1
        while True: # test a particular prime for a solution
            if b == c + 2*num**2:
                found = True
            elif b < c + 2*num**2:
                break
            num+=1
        if found == True:
            break
    if found == False:
        if b !=1:
            print ("Cannot find a solution for: ", b)
            break
print ("Run Time = " , str(time.time() - tStart))

#Cannot find a solution for:  5777
#Run Time =  5.932000160217285

