import time
tStart = time.time()
'''
def BinarySearch(A, value, low, high):
    if high < low:
        return -1 # not found
    mid = int(low + (high - low) / 2)
    if (A[mid] > value):
        return BinarySearch(A, value, low, mid-1)
    elif (A[mid] < value):
        return BinarySearch(A, value, mid+1, high)
    else:
        return mid # found
    return
'''
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
            #temp.append(x)
    return count
maxVal = 0
maxNum = 0
currPhi = 0
currTest  = 0.0
done = 0.0
currentNumber = 25000
'''
filename = "primes.txt"
f = open(filename,"r")
text = f.readline() 
data = ''
while len(text) != 0:
    data = data + text
    text = f.readline() 
primeList = data.split(',')

a = 0
b = len(primeList) -1
while a <= b:
    primeList[a] =  primeList[a].rstrip()
    primeList[a] = int(primeList[a])
    a+=1
'''

print ("time ",str(time.time() - tStart))
print (phi(25000))
print ("time ",str(time.time() - tStart))

while currentNumber <= 50000:
    if isPrime(currentNumber) == True:
    #if BinarySearch(primeList, currentNumber, 0, 78498-1) == 1:
        currentNumber +=1
        continue
    currPhi = phi(currentNumber)
    currTest = currentNumber/currPhi    # n/phi(n)
    #print (currentNumber, "   ",currPhi,"    ", currTest)
    if currentNumber % 1000 == 0:
        print (round(done,2),"%   Current number: ",currentNumber ," Time: ",str(time.time() - tStart))
        done+=0.1
    #print ("n = ",currentNumber, "phi  = ",currPhi, "    ----- n/phi(n) = ",currTest )
    if currTest > maxVal:
        maxVal = currTest
        maxNum = currentNumber
        print ("n = ",currentNumber, "phi  = ",currPhi, "    ----- n/phi(n) = ",currTest )
    currentNumber +=1
print ("maxNum: ", maxNum, "   --- MaxVal: ",maxVal)
print ("Run Time = " , str(time.time() - tStart))


# n =  2310 phi  =  480     ----- n/phi(n) =  4.8125

#510510 5.53938802083
# 2*3*5*7*11*13*17 = 510510
