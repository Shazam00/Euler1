import time
tStart = time.time()

def valueHand(z):
    result = []
    check = z
    values = []
    for x in z:
        if x[0] == "T":
            values.append(10)
        elif x[0] == "J":
            values.append(11)
        elif x[0] == "Q":
            values.append(12)
        elif x[0] == "K":
            values.append(13)
        elif x[0] == "A":
            values.append(14)
        else:
            values.append(int(x[0]))
    values.sort()
    unique = list(set(values))
    unique.sort()
    cardCount = {}
    for x in unique:
        cardCount[x] = 0
    for x in values:
        cardCount[x] = cardCount[x]+1
    
    # royal flush
    if check[0][1] == check[1][1] == check[2][1] == check[3][1] == check[4][1]:
        if values[0] == 10 and values[1] == 11 and values[2] == 12 and values[3] == 13 and values[4] == 14:
            result.append(1)
            result.append("Royal Flush")
            return result
    
    # straight flush
    if check[0][1] == check[1][1] == check[2][1] == check[3][1] == check[4][1]:
        count = 0
        a = []
        a = list(values)
        if a[0] == 2:
            while count < 5:
                if a[count] < 10:
                    a[count] = a[count]+13
                count=count+1
        a.sort()
        if values[0]+1 == values[1] and values[1]+1 == values[2] and values[2]+1 == values[3] and values[3]+1==values[4]:
            result.append(2)
            result.append("Straight Flush")
            return result
    
    # four of a kind
    if check[0][0] == check[1][0] == check[2][0] == check[3][0] == check[4][0]:
        result.append(3)
        result.append("Four of a kind")
        result.append(check[0][0])
        return result
    # full house
    if len(unique) == 2:
        result.append(4)
        result.append("Full house")
        if cardCount[unique[0]] == 3:
            result.append(unique[0])
            result.append(unique[1])
        else:
            result.append(unique[1])
            result.append(unique[0])
        return result
    
    # flush
    if check[0][1] == check[1][1] == check[2][1] == check[3][1] == check[4][1]:
        result.append(5)
        result.append("Flush")
        result.append(check[0][1])
        return result

    # straight
    count = 0
    a = []
    a = list(values)
    if a[0] == 2:
        while count < 5:
            if a[count] < 10:
                a[count] = a[count]+13
            count=count+1
    a.sort()
    if values[0]+1 == values[1] and values[1]+1 == values[2] and values[2]+1 == values[3] and values[3]+1==values[4]:
        result.append(6)
        result.append("Straight")
        return result

    # three of a kind
    for x in cardCount:
        if cardCount[x] == 3:
            result.append(7)
            result.append("Three of a kind")
            result.append(x)
            return result
    
    # two pairs
    if len(unique) == 3:
        result.append(8)
        result.append("2 pair")
        for x in cardCount:
            if cardCount[x] == 2:
                result.append(x)
        return result
    
    # one pair
    if len(unique) == 4:
        result.append(9)
        result.append("1 Pair")
        for x in cardCount:
            if cardCount[x] == 2:
                result.append(x)
        return result

    # high card
    result.append(10)
    result.append("High Card")
    result.append(values)
    
    return result



player1Hands = []
player2Hands = []
filename = "poker54.txt"
f = open(filename,"r")
text = f.readline().rstrip()
temp = []
temp = text.split(" ")
data = []
while len(text) != 0:
    data.append(temp)
    text = f.readline().rstrip()
    temp = text.split(" ")

for x in data:
    player1Hands.append(x[0:5])
    player2Hands.append(x[5:10])

count = 0
p1count = 0
tie = 0
while count < 1000:
    p1result = valueHand(player1Hands[count])
    p2result = valueHand(player2Hands[count])
    if p1result[0] < p2result[0]:
        print(player1Hands[count]," ",player2Hands[count]," -> P1 wins ",p1result)
        p1count= p1count+1
    elif p1result[0] > p2result[0]:
        print(player1Hands[count]," ",player2Hands[count]," -> P2 wins ",p2result)
    else:
        if p1result[0] == 10:
            #print (p1result)
            #print (p1result[2][4])
            #print (p2result)
            #print (p2result[2][4])
            if p1result[2][4] > p2result[2][4]:
                print(player1Hands[count]," ",player2Hands[count]," -> P1 wins ",p1result)
                p1count= p1count+1
            else:
                print(player1Hands[count]," ",player2Hands[count]," -> P2 wins ",p2result)
        elif p1result[0] == 9:
            if p1result[2] > p2result[2]:
                print(player1Hands[count]," ",player2Hands[count]," -> P1 wins ",p1result)
                p1count= p1count+1
            else:
                print(player1Hands[count]," ",player2Hands[count]," -> P2 wins ",p2result)
        else:
            print(player1Hands[count]," ",player2Hands[count]," -> TIE p1 ",p1result, "  p2 ",p2result)
            tie=tie+1
    count=count+1
print (p1count)
print (tie)
   
print ("Run Time = " , str(time.time() - tStart))






