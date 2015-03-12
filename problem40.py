import time
import string
tStart = time.time()
digit = 0
number = 0
accum = 0
while number < 1000001:
    number+=1
    for x in range(len(str(number))):
        digit+=1
        if digit == 1:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 10:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 100:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 1000:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 10000:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 100000:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
        elif digit == 1000000:
            print (digit," ->",str(number)[x])
            accum += int(str(number)[x])
print (accum)
print ("Run Time = " , str(time.time() - tStart))