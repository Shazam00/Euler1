import time
tStart = time.time()

def pentagonal(num):
    return int(num*(3*num-1)/2)

def BinarySearch(A, value, low, high):
    if high < low:
        return -1 # not found
    mid = int(low + (high - low) / 2)
    if (A[mid] > value):
        return BinarySearch(A, value, low, mid-1)
    elif (A[mid] < value):
        return BinarySearch(A, value, mid+1, high)
    else:
        return mid # found
    return

data = []
length = 10000
for x in range(length):
    data.append(pentagonal(x+1))
D = 9999999999
sum = 0
difference = 0
done = 0
for a in range(length-1):
    #print (a)
    if a% 100 ==0:
        print (done," % done --- current number: ", a, " --- current time: ", str(time.time() - tStart))
        done +=1
    for b in range(length-a-2):
        sum = data[a]+data[a+b+1]
        if BinarySearch(data, sum, 0, length-1) != -1:
            difference = data[a+b+1]-data[a]
            #print (data[a+b+1]," + ",data[a], " = ",sum)
            if BinarySearch(data, difference, 0, length-1) != -1:
                print (data[a+b+1]," + ",data[a], " = ",sum, "  > difference = ",difference)
                if difference < D:
                    D = difference

print ("D = ", D)
print ("Run Time = " , str(time.time() - tStart))

# 10  % done --- current number:  1000  --- current time:  112.13499999046326
# 7042750  +  1560090  =  8602840   > difference =  5482660
# 11  % done --- current number:  1100  --- current time:  122.6690001487732


