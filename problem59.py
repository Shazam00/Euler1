import time
tStart = time.time()

def XOR(num1, num2):
    return num1 ^ num2

def encode(text, key):
    count = 0
    result = []
    for i in text:
        result.append(XOR(i,key[count]))
        count= count+1
        if count == len(key):
            count = 0
    return result

filename = "cipher1.txt"
f = open(filename,"r")
data = []
text = ""
text = f.readline() 

temp = text.split(",")

for a in temp:
    data.append(int(a))

print(data)

#97 to 122

found = False
for i in range (97,123):
    for j in range (97,123):
        for k in range (97,123):
            candidate = encode(data, [i,j,k])
            b = ""
            for z in candidate:
                b = b + chr(z)
            if b.find(' the ') != -1:
                print(chr(i),chr(j),chr(k), " = ",b)
                found = True
                break
            if found == True:
                break
        if found == True:
            break
    if found == True:
        break 
#candidate = encode(data, [103,111,100])
sum = 0
for g in candidate:
    sum = sum + g
print ("sum = ",sum)
print ("Run Time = " , str(time.time() - tStart))