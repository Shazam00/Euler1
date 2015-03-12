import time
from fractions import gcd
tStart = time.time()


left = 1/3
right = 1/2
count = 0
size = 12000
for d in range(2, size+1):
    for n in range(1, int(d/2)+1):
        if gcd(n,d) ==1 :
            temp = n/d
            if temp > left and temp < right:
                count = count  + 1
                #print (count,"--- currently at :", d, " of ", size)
print (count)
print (left," ",right)
print ("Run Time = " , str(time.time() - tStart))

# 7295372