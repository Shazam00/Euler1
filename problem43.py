import time
import itertools
tStart = time.time()

def checkProperty(num):
    a = list(num)
    d2 = int( str(a[1]) + str(a[2]) + str(a[3]))
    d3 = int( str(a[2]) + str(a[3]) + str(a[4]))
    d5 = int( str(a[3]) + str(a[4]) + str(a[5]))
    d7 = int( str(a[4]) + str(a[5]) + str(a[6]))
    d11 = int( str(a[5]) + str(a[6]) + str(a[7]))
    d13 = int( str(a[6]) + str(a[7]) + str(a[8]))
    d17 = int( str(a[7]) + str(a[8]) + str(a[9]))
    count = 0
    if d2 % 2 == 0:
        count+=1
    if d3 % 3 == 0:
        count+=1
    if d5 % 5 == 0:
        count+=1
    if d7 % 7 == 0:
        count+=1 
    if d11 % 11 == 0:
        count+=1     
    if d13 % 13 == 0:
        count+=1
    if d17 % 17 == 0:
        count+=1
    if count == 7:
        return True
    return False

def getInt(l):
    s = ""
    for c in l:
        s = s + str(c)
    return int(s)

totalSum = 0
data = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
print ("length = ",len(data))
for x in data:
    if checkProperty(x):
        totalSum += getInt(x)
        print (getInt(x))
        
print("Total Sum: ", totalSum)
print ("Run Time = " , str(time.time() - tStart))

#length =  3628800
#1406357289
#1430952867
#1460357289
#4106357289
#4130952867
#4160357289
#Total Sum:  16695334890
#Run Time =  44.424999952316284


