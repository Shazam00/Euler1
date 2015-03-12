
def even(num):
    return (num/2)
    
def odd(num):
    return (3*num+1)

counter = 1
currNum = 1
maxChain = 0
maxChainNum = 0
curChain = 0
while (counter < 1000000):
    currNum = counter
    currChain = 0
    while (currNum != 1):
        if currNum % 2 == 0:
            currNum = even(currNum)
        else:
            currNum = odd(currNum)
        currChain=currChain+1
    if currChain > maxChain:
        maxChain = currChain
        maxChainNum = counter
    counter=counter+1
print (maxChain)
print (maxChainNum)