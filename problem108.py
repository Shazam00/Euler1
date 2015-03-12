import time
tStart = time.time()



num = 4

x = 1


while x < 10:
    y = 1/4 - 1/x
    if y !=0:
        y=int(1/y)
        print (x, " ",1/y," ",1/x," sum= ",y+1/x)

    x=x+1








print ("Run Time = " , str(time.time() - tStart))