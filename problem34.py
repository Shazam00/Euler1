#problem 34 of Project Euler
#returns Sum of all factorial sum
import time
tStart = time.time()
def getFactorialSum(num):
    sum = 0
    data = str(num)
    length = len(data)
    count = 0
    while count < length:
        if data[count] == '1':
            sum +=1
        elif data[count] == '2':
            sum+=2
        elif data[count] == '3':
            sum+=6        
        elif data[count] == '4':
            sum+=24
        elif data[count] == '5':
            sum+=120
        elif data[count] == '6':
            sum+=720
        elif data[count] == '7':
            sum+=5040
        elif data[count] == '8':
            sum+=40320
        elif data[count] == '9':
            sum+=362880
        elif data[count] == '0':
            sum+=1
        count+=1
    return sum

counter = 3
totalSum = 0
currSum = 0
while counter < 50000:
    currSum = getFactorialSum(counter)
    if currSum == counter:
        totalSum+=counter
        print(counter)
    counter+=1
print("====")
print(totalSum)
print ("Run Time = " , str(time.time() - tStart))