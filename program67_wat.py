import time
import string
tStart = time.time()
f = open("data67.txt", "r").readlines()
values = []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(token)
    values.append(temp)
values.reverse()
z=0
for i in range(0, len(values) - 1):
    j = 0
    for k in values[i+1]:
        values[i+1][j] = max([int(k) + int(values[i][j]), int(k) + int(values[i][j+1])])
        j += 1
        z+=1
print (values[len(values)-1][0])
print ("Run Time = " + str(time.time() - tStart))
print(z)