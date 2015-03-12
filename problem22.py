import time
import string
tStart = time.time()

def getAlphaSum(str):
    sum = 0
    for x in str:
        if x == 'A':
            sum +=1
        elif x == 'B':
            sum+=2
        elif x == 'C':
            sum+=3
        elif x == 'D':
            sum+=4
        elif x == 'E':
            sum+=5
        elif x == 'F':
            sum+=6
        elif x == 'G':
            sum+=7
        elif x == 'H':
            sum+=8
        elif x == 'I':
            sum+=9
        elif x == 'J':
            sum+=10
        elif x == 'K':
            sum+=11
        elif x == 'L':
            sum+=12
        elif x == 'M':
            sum+=13
        elif x == 'N':
            sum+=14
        elif x == 'O':
            sum+=15
        elif x == 'P':
            sum+=16
        elif x == 'Q':
            sum+=17
        elif x == 'R':
            sum+=18
        elif x == 'S':
            sum+=19
        elif x == 'T':
            sum+=20
        elif x == 'U':
            sum+=21
        elif x == 'V':
            sum+=22
        elif x == 'W':
            sum+=23
        elif x == 'X':
            sum+=24
        elif x == 'Y':
            sum+=25
        elif x == 'Z':
            sum+=26
    return sum


filename = "names.txt"
f = open(filename,"r")
text = ""
text = f.readline() 
text = text.replace("\"","")
values = text.split(',')

values.sort()

total = 0
count = 1
for y in values:
    total += count*getAlphaSum(y)
    count+=1
print (total)
print ("Run Time = " + str(time.time() - tStart))











