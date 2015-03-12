import time
tStart = time.time()


def getTriangleNum(num):
    return int(0.5*num*(num+1))

def getPentagonalNum(num):
    return int(0.5*num*(3*num-1))

def getHexagonalNum(num):
    return int(num*(2*num-1))


triangleNumbers = []
for y in range(21):
    triangleNumbers.append(getTriangleNum(y+1))
print (triangleNumbers)

pentagonalNumber = []
for y in range(21):
    pentagonalNumber.append(getPentagonalNum(y+1))
print (pentagonalNumber)

hexagonalNumber = []
for y in range(21):
    hexagonalNumber.append(getHexagonalNum(y+1))
print (hexagonalNumber)


#countT = 285;
#countP = 165;
#countH = 143;

countT = 286;
countP = 165;
countH = 143;

currNumT = getTriangleNum(countT)
currNumP = getPentagonalNum(countP)
currNumH = getHexagonalNum(countH)

print (currNumT)
print (currNumP)
print (currNumH)

#currNumT = 5
#currNumP = 4
#currNumH = 5

iterations = 1

while True:
    if currNumT==currNumP and currNumT==currNumH:
        break;
#    print("fail!")
#    print ("iterations = ", iterations)
#    print ("currentTri = ", currNumT)
#    print ("===========================")
#    print ("Triangle ", currNumT)
#    print ("Pentagonal ", currNumP)
#    print ("Hexagonal ", currNumH)
#    print ("===========================")
    iterations+=1;
    
    # increment the lowest value
    if currNumT < currNumP or currNumT < currNumH:
        countT += 1
        currNumT = getTriangleNum(countT)
    elif currNumP < currNumT or currNumP < currNumH:
        countP += 1
        currNumP = getPentagonalNum(countP)
    elif currNumH < currNumT or currNumH < currNumP:
        countH += 1
        currNumH = getHexagonalNum(countH)
    else:
        print("error")
print("success!")
print ("iterations = ", iterations)
print ("===========================")
print ("Triangle ", countT)
print ("Pentagonal ", countP)
print ("Hexagonal ", countH)
print ("===========================")
print ("result", currNumT)
print ("check")
print (getTriangleNum(countT))
print (getPentagonalNum(countP))
print (getHexagonalNum(countH))

print ("Run Time = " , str(time.time() - tStart))