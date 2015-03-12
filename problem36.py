import math
import time
tStart = time.time()
def convert(iNumber):
    bin = ""
    oNumber = iNumber
    while (iNumber>0):
        if (iNumber%2):
            bin = "1"+ bin
        else:
            bin = "0"+ bin
        iNumber = math.floor(iNumber/2)
    return bin
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
finalSum = 0
count = 1
c = 0
while count < 1000000:
    if (isPalindrome(count) == True) & (isPalindrome(convert(count))):
        finalSum+=count
        c+=1
    count+=1
print(c)
print(finalSum)
print ("Run Time = " , str(time.time() - tStart))