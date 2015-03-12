# inefficient solution to problem 145
# see problem 145a for the faster solution
import time
tStart = time.time()
sum = 0
oddCheck = 1
count = 0
done = 0.0
list = []
for x in range(1000000000):
    if x % 10 == 0:
        if x % 1000000 == 0:
            done+=0.1
            print(round(done,1),"%  --","Current Total: ", count, "  Current number: ", x , "listSize", len(list)," Time: ",str(time.time() - tStart))
        continue
    sum = x + int(str(x)[::-1])
    if sum in list:
        list.remove(sum)
        count = count + 1
    else:
        oddCheck = 1
        for y in str(sum):
            oddCheck = oddCheck * int(y)
            if oddCheck %2 == 0:
                break
        if oddCheck %2 != 0:
            count=count+1
            list.append(sum)
print ("Total Odd: ", count)
print ("Run Time = " , str(time.time() - tStart))