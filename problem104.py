"""
import time
tStart = time.time()


def isPandigital(num):
    a = list(set(list(str(num))));
    a.sort()
    if len(a) != 9:
        return False
    
    if len(list(str(num))) > int(a[len(a)-1]):
        return False
    count = 1
    for n in a:
        if int(n) != count:
            return False
        else:
            count+=1
    return True


first = 1
second = 1
current = 0
count = 3

print(1)
print(2)
while count < 999999999:
    current = first + second
    if len(str(current)) >=9:
        if isPandigital(int(str(current)[0:9])):
            #print (count,"  ",current,"  > Front Match")
            print(count)
            if isPandigital(int(str(current)[len(str(current))-9:len(str(current))])):
                print (count,"  ",current,"  > End Match")
                break
        #print (count,"  ",current,"  > No Match")
    #else:
    #    print (count,"  ",current,"  > Too Short")
    done = 0.0
    if count % 800 == 0:
        done+=1
        print(round(done,2),"%  --","  Current number: ", count ," Time: ",str(time.time() - tStart))
    
    first = second
    second = current
    count = count+1
print (count)


print ("Run Time = " , str(time.time() - tStart))
"""

import math

def GetDigits(n):
    Digits = []
    while n > 0:
        Digits.append(n % 10)
        n = int(n / 10)
    return Digits

def Solve(): 
    a, b = 0, 1
    i = 2
    Phi = (1 + math.sqrt(5)) / 2
    while True:
        c = (a + b) % (10 ** 9)
        a, b = b, c
        if i % 1000 == 0:
            print(i)
        LastDigits = GetDigits(c)
        LastDigits.sort()
        if LastDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Fib(", i, ") - ", "Last digits ok")
        else:
            i = i + 1
            continue
        LogFib = i * math.log(Phi, 10) - math.log(math.sqrt(5), 10);  
        d = int(pow(10, LogFib - int(LogFib - 8)))
        FirstDigits = GetDigits(d)
        FirstDigits.sort()
        if FirstDigits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Fib(", i, ") - ", "First digits ok")
        else:
            i = i + 1
            continue
        break
    print("\n\n\nSolution : Fib(", i, ")",);
    return
print ("PROJECT EULER 104:");
Solve();
