import time
tStart = time.time()
size = 100
array = []
temp = 0
for a in range(size-1):
    for b in range(size-1):
      temp = (a+2)**(b+2)
      if temp not in array:
          array.append(temp)
print(len(array))
print ("Run Time = " , str(time.time() - tStart))