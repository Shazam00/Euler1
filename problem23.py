import time
import string
tStart = time.time()

def binarySearch(A, value, low, high):     #pass in the list, value to be searched, and the lower and upper limits of the list
    while low <= high:                     #loop until the list high is lower then the low value (i.e. search is finished)
        mid = int((low + high) / 2);            #determine the middle of the list
        
        if A[mid] > value:                 #is the value less then the middle? redefine the parameters of the search
            high = mid - 1;
        elif A[mid] < value:               #is the middle less then the value to be found? If so redefine the parameters
            low = mid + 1;
        else:
            return mid;                    #found       
    return -1                              # not found 

f = open("data23.txt","r")
text = f.readline() 
abundant = []
while len(text) != 0:
    abundant.append(text)
    text = f.readline() 
for x in range(len(abundant)):
    abundant[x] = int(abundant[x].replace("\n",""))
a = 0
length = len(abundant)
result = 0
counter = 0
AbundantSum = False
temp = 0
while counter <= 29000 :  #loop through each number from 1 to 28122
    counter+=1
    AbundantSum = False
    for a in range(length):   #pivot
        temp = counter - abundant[a]                                # get value to find in list
        if temp < 12:
            break
        if binarySearch(abundant,temp,0,len(abundant)-1) != -1:     
            # number is found
            #print("True==> ",counter,"= ", abundant[a]," + ",abundant[binarySearch(abundant,temp,0,len(abundant)-1)])
            AbundantSum = True
            break               #break after the value is found
    if AbundantSum == False:
        result += counter
        #print("Non==> ",result," @ ",counter)
print(result)
print ("Run Time = " , str(time.time() - tStart))