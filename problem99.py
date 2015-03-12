import time
import math
tStart = time.time()

filename = "base_exp99.txt"
f = open(filename,"r")
text = f.readline().rstrip()
temp = []
temp = text.split(",")
data = []
while len(text) != 0:
    data.append(temp)
    text = f.readline().rstrip()
    temp = text.split(",")
count = 0
x = 0
while x < len(data):
    data[x][0] = int(data[x][0])
    data[x][1] = int(data[x][1])
    x=x+1

currMax = 0
linenum = 0
count = 0 

while count < len(data):
    if data[count][1]*math.log(data[count][0]) > currMax:
        currMax = data[count][1]*math.log(data[count][0])
        linenum = count + 1
    print (data[count])
    count = count+1

print (linenum)

#line 709
print ("Run Time = " , str(time.time() - tStart))
