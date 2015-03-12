import time
import math
tStart = time.time()
closestArea = 0
closestRec = 0
difference = 2000000
target = difference
for x in range(1,100):
    for y in range(1,100):
        # generate all the rectangles for a particular map size
        sum = int((x*x+x)*(y*y+y)/4)
        # check if current map is closest to target
        if difference > math.fabs(target-sum):
            closestRec = sum
            closestArea = x*y
            difference = math.fabs(target-sum)
            print ("======================")
            print ("(",x,",",y,")")
            print ("closestRec: ",closestRec)
            print ("closestArea: ",closestArea)
            print ("difference: ",difference)
        if sum > target+difference:
            break
print ("Run Time = " , str(time.time() - tStart))

