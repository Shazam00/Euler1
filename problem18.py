import math
import time
tStart = time.time()
def getPath(iNumber):
    bin = ""
    oNumber = iNumber
    while (iNumber>0):
        if (iNumber%2):
            bin = "1"+ bin
        else:
            bin = "0"+ bin
        iNumber = math.floor(iNumber/2)
    while len(bin) != 15:
        bin = "0"+bin
    return bin

def convert(bin,data):
    position = 0
    input = str(bin)
    max = 75
    count = 1
    while count <= 14:
        if bin[count] == "0":
            position = position+count+1
        else:
            position = position+count
        max+=data[position]
        count+=1
    return max

filename = "data18.txt"
f = open(filename,"r")
text = f.readline() 
data = []
while len(text) != 0:
    data.append(text)
    text = f.readline() 
for x in range(120):
    data[x] = int(data[x][:2])

maxSum =0
count = 0
currSum = 0
pos = 0
while count < 16384:
    currSum = convert(getPath(count),data)
    if currSum > maxSum:
        maxSum = currSum
        pos = count
    count+=1
print("position: ",pos)
print("Sum :",maxSum)
print ("Run Time = " , str(time.time() - tStart))