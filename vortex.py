pattern = "124875"
def getSum(num):        # num = int
    number = str(num)
    value = 0
    length = len(str(number))
    count = 0
    while count < length:
        value = value + int(str(number[count]))
        count = count + 1
    return value        # returns int
def getVortexSum(num):
    result = 0
    value = num
    while value > 9:
        value = getSum(value)
    return value
counter = 1
x = 1
while counter < 50:
    print(x," --- ", getVortexSum(x))
    x = x+x
    counter = counter +1
    