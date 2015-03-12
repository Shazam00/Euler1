import time
tStart = time.time()

def isPandigital(num,length):
    a = list(set(list(str(num))));
    a.sort()
    if len(list(str(num))) > int(a[len(a)-1]):
        return False
    if len(list(str(num))) != length:
        return False
    count = 1
    for n in a:
        if int(n) != count:
            return False
        else:
            count+=1
    return True
base = 1
multiplier = 1
product = 1
check = 0
store = []
sum = 0
count=0
while base < 1000:
    multiplier = 1
    while multiplier < 9999:
        product = base*multiplier
        check = int(str(base)+ str(multiplier)+ str(product))
        #print(base, " x " ,multiplier, " = ", product, " -> ", check)
        if isPandigital(check,9):
            if (product in store) == False:
                print(base, ".",multiplier,".",product)
                store.append(product)
        count+=1
        multiplier +=1
    base +=1
print(count)
print(len(store))
for x in store:
    sum +=x
print ("total sum: ", sum)
print ("Run Time = " , str(time.time() - tStart))



