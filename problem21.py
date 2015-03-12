import time
tStart = time.time()
def getDivisors(num):
    divisors = []
    currValue = 1
    maxValue = num/2
    while currValue <= maxValue:
        if num % currValue == 0:
            divisors.append(currValue)
        currValue+=1
    #divisors.append(num)
    return divisors
def d(num):
    value = 0
    a = getDivisors(num)
    for x in a:
        value+= x
    return value
result = []
count = 1
while count < 10000:
    a = d(count)
    b = d(a)
    #print(count," ",b)
    if (count==b) & (a != b) & (a<10000) & (count<10000):
        result.append(a)
        result.append(b)
    count+=1
print(result)
final = 0
for x in result:
    final+= x
print(int(final/2))
print ("Run Time = " , str(time.time() - tStart))