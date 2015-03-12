import time
tStart = time.time()

#build input
a = 1
l= [2,1,2]
b = 4
while a  <= 97:
    if a%3==0:
        l.append(b)
        b=b+2
    else:
        l.append(1)
    a=a+1
    
#contFrac = [2,1,2,1,1,4,1,1,6,1]
contFrac = l

#input
# contFrac = []    # e.g, [1,2,2,2,2,..,2] = sqrt(2)

# build fraction
w=0 # whole number
n=0 # numerator
d=0 # denominator
contFrac.reverse()
length = len(contFrac)
count=0
while count < length:
    if count == 0: #initial value
        w=contFrac[0]   #set initial whole number
        n=1             # set initial numerator
        d=w             # set initial denominator
        print("Step ",count,": ",contFrac[count]," ",n," / ",d)
    else:
        if count != length-1: # if this isn't the last digit
            w=contFrac[count]   #set new whole number
            n = d*w+n               # calculate new n
            #swap n and d
            temp = n
            n = d
            d = temp
        else:
            w=contFrac[count]   #set new whole number
        print("Step ",count,": ",contFrac[count]," ",n," / ",d)
    count=count+1
print("Steps ",length)
print("Result : ",w," + ",n," / ",d)
print("Improper Fraction :",w*d+n," / ", d)
print("Decimal :",(w*d+n)/d)

top = str(w*d+n)
sum = 0
for a in top:
    sum = sum + int(a)

print("Sum numerator : ",sum)
print ("Run Time = " , str(time.time() - tStart))
