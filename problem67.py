#edit this

import math
import time
import string
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
    while len(bin) != 100:
        bin = "0"+bin
    return bin

def convert(bin,data):
    position = 0
    input = str(bin)
    max = 75
    count = 1
    while count <= 99:
        if bin[count] == "0":
            position = position+count+1
        else:
            position = position+count
        max+=data[position]
        count+=1
    return max

filename = "data67.txt"
f = open(filename,"r")
print("file opened")
data = []
text = ""
text = f.readline() 
height = 1
rowNode = 1
temp = []
while len(text) != 0:
    temp = text.split(" ")
    rowNode = 0
    while rowNode <= height-1:
        data.append(temp[rowNode])
        rowNode+=1
    height+=1
    text = f.readline()
for x in range(len(data)):
   data[x] = int(data[x][:2])
#print(data)
print("data read")
maxSum = 0
count = 1
currSum = 0
pos = 0
print("calculating....")
while count < 100:
    currSum = convert(getPath(count),data)
    if currSum > maxSum:
        maxSum = currSum
        pos = count
        print("Position: ",pos, " | Sum: ",maxSum)
    count+=1
print("position: ",pos)
print("Sum :",maxSum)
print ("Run Time = " , str(time.time() - tStart))