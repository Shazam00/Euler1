import time
tStart = time.time()
def doesTriangleContainOrigin(triangle):
    xp = False
    xn = False
    yp = False
    yn = False
    result = False
    for a in range(3):
        # find slope and intercepts
        if a == 0:
            x1 = triangle[0]
            x2 = triangle[2]
            y1 = triangle[1]
            y2 = triangle[3]
        elif a ==1:
            x1 = triangle[2]
            x2 = triangle[4]
            y1 = triangle[3]
            y2 = triangle[5]
        else:
            x1 = triangle[0]
            x2 = triangle[4]
            y1 = triangle[1]
            y2 = triangle[5]
        # check if the slope is 0 or infinity
        if x2-x1 != 0:
            slope = (y2-y1)/(x2-x1)
        else:
            slope = 99
        if slope == 0:
            slope = 0.00001
        yint = -1*(slope*x1)+y1
        xint = -1*yint/slope
        #check each of the 4 axis for an intersection
        if xint > 0:
            if xint <= x1 or xint <= x2:
                xp = True
        if xint < 0:
            if xint >= x1 or xint >= x2:
                xn = True
        if yint > 0:
            if yint <= y1 or yint <= y2:
                yp = True
        if yint < 0:
            if yint >= y1 or yint >= y2:
                yn = True
    if yp == True and xp == True and yn == True and xn == True:
        result = True
    return result
filename = "triangles102.txt"
f = open(filename,"r")
print("file opened")
data = []
text = ""
height = 1
temp = []
text = f.readline() 
while len(text) != 0:
    temp = text.split(",")
    temp[5] = temp[5].rstrip()
    for x in range(6):
        temp[x] = int(temp[x])
    text = f.readline()
    data.append(temp)
count = 0
for c in data:
    if doesTriangleContainOrigin(c):
        count+=1
print("total count: ",count)
print ("Run Time = " , str(time.time() - tStart))
