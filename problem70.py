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

def gcd(num1, num2): # num1 > num2
    for i in range(2,num2+1):
        if num2 % i == 0 and num1 % i == 0:
            result = i
            if result > 1:
                return -1
    return 1

def phi(num):
    count = 1
    temp = [1]
    for x in range(2, num):
        if gcd(num,x) == 1:
            count+=1
            temp.append(x)
    return count





print ("Run Time = " , str(time.time() - tStart))