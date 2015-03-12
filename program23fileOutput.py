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

def sum(n):
    result = 0
    for x in n:
        result +=x
    return result

f = open('data23.txt', 'w')


#abundant = [1,2,5,6,8,9,12,15,20]
abundant = []
counter = 1

while counter < 29000:
    if counter < sum(getDivisors(counter)):
        abundant.append(counter)
        f.write(str(counter))
        f.write("\n")
    counter+=1
f.close()

print("Abundant Numbers List Built.")
print ("Run Time = " , str(time.time() - tStart))