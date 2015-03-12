import time
tStart = time.time()

def printBoard(b):
    for x in b:
        print (x)

filename = "sudoku96.txt"
f = open(filename,"r")
print("file opened")
data = []
text = ""
text = f.readline() 
height = 1
rowNode = 1
temp = []
while len(text) != 0:
    temp = text.split()
    if temp[0] == "Grid":
        data.append("Grid "+temp[1] )
    else:
        data.append(temp)
    text = f.readline()
print(data)
print("Load 1st grid")

Board = []
count = 0
while data[count] != "Grid 01":
    count +=1
    
count +=1
n = 0
while n < 9:
    Board.append(data[count+n])
    n=n+1
printBoard(Board)

result = []

r = 0
s = 0
while r < 9:
    s = 0
    result.append([])
    while s < 9:
        result[r].append("0123456789")
        s=s+1
    r = r + 1

print ("Result")

printBoard(result)
#print(result)




print ("Run Time = " , str(time.time() - tStart))
