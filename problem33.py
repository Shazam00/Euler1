import time
tStart = time.time()

def inproperCancelling(n,d):
    x = list(str(n))
    y = list(str(d))
    z = []
    if x[0] == y[1]:
        del x[0]
        del y[1]
    elif x[1] == y[0]:
        del x[1]
        del y[0]
    else:
        return [1,1]
    z.append(int(x[0]))
    z.append(int(y[0]))
    return z
count=0
a = 0
b = 0
temp = []
for numerator in range(90):
    for denominator in range(90):
        if denominator > numerator:
            temp = inproperCancelling(numerator+10,denominator+10)
            a = temp[0]
            b = temp[1]
            if b !=0:
                #print (a," / ",b,"  --- ",numerator+10," / ",denominator+10, " check-> ",a/b, " ? ",(numerator+10)/(denominator+10))
                if (a/b) == ((numerator+10)/(denominator+10)):
                    #print (a," / ",b)
                    print (a," / ",b,"  --- ",numerator+10," / ",denominator+10, " check-> ",a/b, " ? ",(numerator+10)/(denominator+10))
                    count+=1 

print("total count: ",count)
print ("Run Time = " , str(time.time() - tStart))




