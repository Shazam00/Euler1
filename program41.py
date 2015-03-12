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
def isPandigital(num):
    result = False
    a = list(set(list(str(num))));
    a.sort()
    if len(list(str(num))) > int(a[len(a)-1]):
        return False
    count = 1
    for n in a:
        if int(n) != count:
            return False
        else:
            count+=1
    if isPrime(num):
        result = True
    else:
        result = False
    return result
number = 1
done = 0.0
while True:
    if number % 80000 == 0:
        done+=1
        print(round(done,2),"%  --","  Current number: ", number ," Time: ",str(time.time() - tStart))
    if isPandigital(number):
        print(number)
    number = number + 1
    if number > 8000000:
        break
print ("Run Time = " , str(time.time() - tStart))

# 7652413
