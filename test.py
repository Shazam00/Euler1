#!/usr/bin/env python
import time

from fractions import gcd
#import gmpy
tStart = time.time()

x = 36
y = 77

sum = int((x*x+x)*(y*y+y)/4)

print (sum)
    

print ("Run Time = " , str(time.time() - tStart))

# 428570