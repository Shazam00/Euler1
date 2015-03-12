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

def isTruncPrime(num):
    result = True
    temp = str(num)
    currNum = str(num)
    while len(currNum) > 0:
        if isPrime(int(currNum)):
            currNum = str(currNum)[1:]
        else:
            result = False
            break
    currNum = temp
    while len(currNum) > 0:
        if isPrime(int(currNum)):
            currNum = str(currNum)[:-1]
        else:
            result = False
            break
    return result
count = 0
sum = 0
done = 0
for x in range(1000000):
    if isTruncPrime(x+10) == True:
        print(x+10)
        count+=1
        sum+=x
    #if x % 10000 == 0:
    #    done+=1
    #    print(round(done),"%  --","Current Total: ", count, "  Current number: ", x ," Time: ",str(time.time() - tStart))
        
print("=====")
print("total:",count)
print("sum:",sum)
print ("Run Time = " , str(time.time() - tStart))

'''
23
37
53
73
313
317
373
797
3137
3797
739397

sum = 748317
'''