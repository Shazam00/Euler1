import time
tStart = time.time()


def C(n,r):
    return  int(Fact(n)/((Fact(r))*Fact(n-r)))
def Fact(num):
    if num == 0:
        return 1
    if num < 0:
        return -1
    if num != 1:
        num = num * (Fact(num-1))
    return num
count = 0
for a in range(100):
    for b in range(a):
        #print (a+1, " C ",b+1)
        if C(a+1,b+1) > 1000000:
            count+=1
print (count)
print ("Run Time = " , str(time.time() - tStart))

# 4075
# Run Time =  0.2369999885559082
