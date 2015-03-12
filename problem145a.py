import time
tStart = time.time()
count = 0
done = 0.0
word = []
odd = True
for x in range(1000000000):
    if x % 10 == 0 or int(str(x)[::-1]) < x :
        if x % 1000000 == 0:
            done+=0.1
            print(round(done,1),"%  --","Current Total: ", count, "  Current number: ", x ," Time: ",str(time.time() - tStart))
        continue
    word = list(str( x + int(str(x)[::-1])))
    for y in word:
        if y in ['2','4','6','8','0']:
            odd = False
            break
    if odd == True:
        count=count+2
    else:
        odd = True
print ("Total Odd: ", count)
print ("Run Time = " , str(time.time() - tStart))