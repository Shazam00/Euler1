import time
tStart = time.time()

def isPalindrome(input):
    isTrue = True
    val = str(input)
    length = len(val)-1
    count=0
    while count < length:
        if val[count] != val[length - count]:
            isTrue = False
        count+=1
    return isTrue

def reverseThenAdd(num):
    return  num + int(str(num)[::-1])

count = 0
iter = 0
currNum = 0
for x in range(10000):
    currNum = x+1
    iter = 0
    #print(x+1)
    while iter < 50:
        currNum = reverseThenAdd(currNum)
        #print("-->",currNum)
        iter+=1
        if isPalindrome(currNum):
            #print("> ",x+1," -> ",currNum, "  iter: ",iter)
            break
        if iter == 50:
            print ("> ",x+1)
            count+=1
        
print("total count: ", count)
print ("Run Time = " , str(time.time() - tStart))

#249

