


def p(n):
    print (n)

def getSum(size, n):
    total = 0;
    if (size%n) == 0:
        total = size/n
    else:
        total = int(size/n)
    return total
    

n= 5
count = 0
print (1)
for i in range(n):
    print (i)
    print (str(n-i-1) + "  <--")
    ##    count +=1
        
print (" total = " + str(count))

print(getSum(5,3))


'''fgjg

p(n)

for 0 to n as i

    count i + p(n-i)  



fgdfgfg
'''





