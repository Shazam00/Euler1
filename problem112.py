import time
tStart = time.time()

def isBouncy(num):
    inc = False
    dec = False
    data = list(str(num))
    for a in range(len(data)):
        data[a] = int(data[a])    
    for a in range(len(data)-1):
        if data[a+1] > data[a]:
            inc = True
        elif  data[a+1] < data[a]:
            dec = True
    if inc == True and dec == True:
        result = True
    else:
        result = False
    return result

count = 0
currNum = 100
while currNum <= 10000000:
    if isBouncy(currNum) == True:
        count+=1
    if count/currNum >= 0.99:
        print("break")
        break
    currNum+=1
print("total bouncy: ",count)
print("total count: ",currNum)
print("proportion bouncy: ",round(count/(currNum),5))

print ("Run Time = " , str(time.time() - tStart))


# total bouncy:  1571130
# total count:  1587000
# proportion bouncy:  0.99
# Run Time =  14.786999940872192



