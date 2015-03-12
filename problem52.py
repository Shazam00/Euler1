import time
tStart = time.time()

def digitMatch(a,b):
    result = False
    A = list(str(a))
    B = list(str(b))
    A.sort()
    B.sort()
    if A == B:
        result = True
    return result
for x in range(1000000):
    if digitMatch(x, 2*x):
        if digitMatch(x, 3*x):
            if digitMatch(x, 4*x):
                if digitMatch(x, 5*x):
                    if digitMatch(x, 6*x):
                        print (x)
print ("Run Time = " , str(time.time() - tStart))