import time
tStart = time.time()
currMax = 0
MaxNum = 0
num = 770
count =0
while num < 1000:
    count = 0
    if num%2 != 0:
        num+=1
        continue
    for i in range(num):
        for j in range(num-i):
            for k in range(num-i-j):
                if (i+1)+(j+1)+(k+1) == num:
                    #print (i+1," ", j+1, " ", k+1)
                    if (i+1)**2+(j+1)**2==(k+1)**2:
                        count+=1
    if count >currMax:
        currMax = count
        MaxNum = num
    print("current num: ",num, "current max: ",currMax, " @ ", MaxNum)
    num+=1
print ("Run Time = " , str(time.time() - tStart))
# current num:  439 current max:  10  @  420
# current num:  660 current max:  10  @  660
# current num:  720 current max:  12  @  720
#current num:  840 current max:  16  @  840

#840