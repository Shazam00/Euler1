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

totalDiagonal = []
maxLength = 99999
count = 0
for x in range(maxLength-1):
    length = x+1
    if (length) %2==0:
        continue
    totalDiagonal.append(length**2+length+1)        #topRight
    if isPrime(totalDiagonal[-1]) == True:
            count+=1
    totalDiagonal.append(length**2+2*(length+1))    #topLeft
    if isPrime(totalDiagonal[-1]) == True:
            count+=1
    totalDiagonal.append(length**2+3*(length+1))    #bottomRight
    if isPrime(totalDiagonal[-1]) == True:
            count+=1
    totalDiagonal.append(length**2+4*(length+1))    #bottomLeft
    if isPrime(totalDiagonal[-1]) == True:
            count+=1
    print ("length = ",length+2, " => ",count, " / ", len(totalDiagonal)+1 , " = ", count/(len(totalDiagonal)+1))
    if count/(len(totalDiagonal)+1) < 0.1:
        break

print ("Run Time = " , str(time.time() - tStart))

# length =  26239  =>  5248  /  52477  =  0.10000571679021286
# length =  26241  =>  5248  /  52481  =  0.09999809454850327
# Run Time =  8.253000020980835




