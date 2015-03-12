import time
tStart = time.time()

base = 1
count = 0
for x in range(50):
    #print(x+1)
    power = x+1
    #print ("> ",len(list(str(base**power)))," - ",power)
    base =1
    while len(list(str(base**power))) <= power:
        #print ("check b:",base)
        if len(list(str(base**power))) == power:
            print (base," ^ ",power," = ",base**power)
            count+=1
        base+=1

print ("total count: ",count)
print ("Run Time = " , str(time.time() - tStart))

# 49