import time
tStart = time.time()
def Factorial(n):
    if n < 2:
        return 1
    else:
        return n*Factorial(n-1)
def DigitFactSum(n):
    a = list(str(n))
    sum = 0
    for b in a:
        sum = sum + Factorial(int(b))
    return sum
number = 1
count = 0
while number < 1000000:
    chainSet = []
    next = DigitFactSum(number)
    while next != number:
        chainSet.append(next)
        next = DigitFactSum(next)
        if next in chainSet:
            chainSet.append(next)
            break
    if len(chainSet) == 60:
        print(number, " ",len(chainSet)," ",chainSet)
        count = count + 1
    number = number + 1
print (count)
print ("Run Time = " , str(time.time() - tStart))
