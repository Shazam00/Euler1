import time
from fractions import gcd
#import gmpy
tStart = time.time()


target = 3/7

count = 999998
current = 0
n = 0
while count > 1:
    #print (count)
    result = count/999999
    if result > current and result < target and gcd(count,999999):
        current = result 
        n = count
    count = count - 1

print (n)

print ("Run Time = " , str(time.time() - tStart))

# 428570
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8