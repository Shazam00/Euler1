import time
tStart = time.time()

current = 1
s={}
target = "012334556789"
while current < 10000:
    cubed = current**3
    numList = list(str(cubed))
    numList.sort()
    string = ""
    for x in numList:
        string = string + x 
    if string in s:
        s[string] =  s[string] + 1
    else:
        s[string] = 1
    
    if target == string:
        print(current, "^3 =", cubed)    
    
    current = current + 1

for x in s:
    if s[x] == 5:
        print (x)


print ("Run Time = " , str(time.time() - tStart))