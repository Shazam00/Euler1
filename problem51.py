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

def Dec2Bin(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr
decimalMask = 100
binaryMask = []
currNum = 100000
while currNum < 200000:
    maskLength = 2**len(str(currNum)) - 2
    count = 1
    binaryMask = []
    primeSet = []
    while count <= maskLength:
        temp = Dec2Bin(count)
        while len(temp) != len(str(currNum)):
            temp = "0"+ temp
        binaryMask.append(temp)
        count = count + 1
    for a in binaryMask:    # for each binary mask per base
        mask = list(a)
        base = list(str(currNum))
        primeSet = []       # reset the prime set
        x = 0
        l = 0
        while x < len(mask):
            if mask[x] == "1":
                base[x] = "*"
                l = l + 1
            x=x+1
        # build test number
        current = 0
        while current < 10:
            # create number to test
            testNum = ""
            for x in base:
                if x == "*":
                    testNum = testNum + str(current)
                else:
                    testNum = testNum + x
            if testNum[0] == "0":
                current = current + 1
                continue
            
            temp = list(temp)
            index = 0
            x = 0
            # test if the number is prime
            if isPrime(int(testNum)) == True:
                primeSet.append(testNum)
            #    print (temp," ",testNum, " Prime")
            #else:
            #    print (temp," ",testNum)
            current = current + 1
        if len(primeSet) > 6:
            print (currNum," ",base," Prime Count: ",len(primeSet)," > ",primeSet)
    currNum = currNum + 1
print ("Run Time = " , str(time.time() - tStart))

#120303   ['*', '2', '*', '3', '*', '3']  Prime Count:  8  >  ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']
