#program 12 for Project Euler
def getDivisors(num):
    divisors = []
    currValue = 1
    maxValue = num/2
    while currValue <= maxValue:
        if num % currValue == 0:
            divisors.append(currValue)
        currValue+=1
    divisors.append(num)
    return divisors

def getDivisorsNum(num):
    divisors = 0
    currValue = 1
    maxValue = num/2
    iter=0
    while currValue <= maxValue:
        if num % currValue == 0:
            divisors+=1
        currValue+=1
        iter+=1
        if divisors >=500: break
    divisors+=1
    print (iter)
    return divisors

def getTriangleNum(num):
    result = 0
    for x in range(num+1):
        result+=x 
    return result

def getTriangle(num):
    result = 1
    value = num
    while value != 0:
        value = value - result
        result +=1
    return result-1

print(getDivisorsNum(76576500))
counter = 4000
currDivisor = 0
currMaxNum = 2078
currMaxDivisors = 1
triangle = 7998000
while counter < 5000:   
    triangle=triangle + counter
    currDivisor = getDivisorsNum(triangle)
    #currDivisor = getDivisorsNum(getTriangleNum(counter))
    #if currDivisor > currMaxDivisors:
    #    currMaxDivisors = currDivisor
    #    currMaxNum = getTriangleNum(counter)
    #    print("Divisors: ",currMaxDivisors, " --> ",currMaxNum, "@" , counter)
    counter+=1
    print(counter, "  ",currDivisor )
    #if currMaxDivisors >=500:
    #    print("break")
    #    break
print("Triangle number: ",currMaxNum)
print("Divisors: ",currMaxDivisors)
print("counter value of :", getTriangle(currMaxNum) )

print("------ set values at -------")
print("counter: ",getTriangle(currMaxNum))
print("currMaxNum: ",getTriangle(currMaxNum)-1)
print("currMaxDivisors: ",currMaxDivisors-1)
print("triangle: ",currMaxNum-getTriangle(currMaxNum))