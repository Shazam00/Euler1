#problem 30 of Project Euler
#returns Sum of all fifth power Sums
import time
tStart = time.time()
def getFifthPowerSum(num):
    sum = 0
    data = str(num)
    length = len(data)
    count = 0
    while count < length:
        if data[count] == '1':
            sum +=1
        elif data[count] == '2':
            sum+=32
        elif data[count] == '3':
            sum+=243        
        elif data[count] == '4':
            sum+=1024
        elif data[count] == '5':
            sum+=3125
        elif data[count] == '6':
            sum+=7776
        elif data[count] == '7':
            sum+=16807
        elif data[count] == '8':
            sum+=32768
        elif data[count] == '9':
            sum+=59049
        elif data[count] == '0':
            sum+=0
        count+=1
    return sum

counter = 3
totalSum = 0
currSum = 0
while counter < 200000:
    currSum = getFifthPowerSum(counter)
    if currSum == counter:
        totalSum+=counter
        print(counter)
    counter+=1
print("====")
print(totalSum)
print ("Run Time = " , str(time.time() - tStart))