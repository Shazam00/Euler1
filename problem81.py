import time
tStart = time.time()


filename = "matrix81.txt"
f = open(filename,"r")
text = f.readline().rstrip()
temp = []
temp = text.split(",")
data = []
while len(text) != 0:
    data.append(temp)
    text = f.readline().rstrip()
    temp = text.split(",")

x = 0
y = 0
while x < 80:
    y = 0
    while y < 80:
        data[x][y] = int(data[x][y])
        y=y+1
    x=x+1

count = 0
while count < len(data):
    data[count].append(99999999)
    count = count+1
count = 0
data.append([])
while count < len(data):
    data[80].append(99999999)
    count = count +1

data[79][80] =0

column = 79
row = 79
while row >= 0:
    column = 79
    while column >= 0:
        if data[row+1][column] <= data[row][column+1]:
            data[row][column] = data[row][column] + data[row+1][column]
        else:
            data[row][column] = data[row][column] + data[row][column+1]
        column=column-1
    row=row-1
count = 0
while count < len(data):
    print (data[count])
    count = count+1
print (len(data))
print (data[0][0])

#427337
print ("Run Time = " , str(time.time() - tStart))







