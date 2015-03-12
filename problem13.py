#problem 13 of Project Euler
#get the sum of the 100 50-digit number in data13.txt
filename = "data13.txt"
f = open(filename,"r")
text = f.readline() 
data = []
while len(text) != 0:
    data.append(text)
    text = f.readline() 
FinalResult = []
carrySTR = ""
toCopy = 0
carry = 0
y = 49
while y >=0:                           # loop through every column
    for x in range(100):                        # loop through every row
        carry = carry + int(data[x][y])         # adds the column of digits to the existing carry value     
    carrySTR = str(carry)                       # convert carry to string
    toCopy = int(carrySTR[len(carrySTR)-1])     # fetch the last digit of the carry
    FinalResult.append(toCopy)                  #     and adds it to the final result
    carry = (carry - toCopy)                     # calculate the new carry for the next column          
    carry = int(carry /10)
    y-=1
FinalResult.append(carry)
FinalResult.reverse()
print(FinalResult)