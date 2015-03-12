import random

def getColor(n):
    sum =0                 
    for i in range(7):
        sum += colors[i]
        if n <= sum:
            return i
    return i

colors = [10,10,10,10,10,10,10]
temp = [0,0,0,0,0,0,0]

current = 1;
runs = 999999
distinct = 0.0

while (current < runs):
    colors = [10,10,10,10,10,10,10]
    temp = [0,0,0,0,0,0,0]
    sum = 70
    test = 0 
    for i in range(20):
        test = random.randint(1,sum)
        remove = getColor(test)
        colors[remove] -=1
        temp[remove]+=1
        sum -=1
    for i in temp:
        if i!=0:
            distinct +=1
    current +=1   
    print (str(current) + " ===>  " + str(distinct/current))
    
#print (colors)
#print (temp)


print (str(distinct) + " / " + str(runs))
print (distinct/runs)




