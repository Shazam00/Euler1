import time
import random
tStart = time.time()

'''
9 4-sided dice

6 6-sided dice

what is the prob that the pyramidal dice user win

answer to 7 decimal places
0.abcdefg

0.573144076783
'''

def pyramid():
    sum = 0
    for x in range(9):
        sum = sum + random.randint(1,4)
    return sum

def cube():
    sum = 0
    for x in range(6):
        sum = sum + random.randint(1,6)
    return sum

winsP = 0
games = 0
done = 1
for x in range(10000000):
    games +=1
    if pyramid() > cube():
        winsP +=1
    if x % 100000 == 0:
        done+=1
        print(done,"%  --","wins/games (",winsP,"/",games,")   ===== win percent: ", winsP/games )
    
print ("Total wins : ",winsP)
print ("Total games: ",games)
print ("win percent: ", winsP/games)

print ("Run Time = " , str(time.time() - tStart))
#http://topps.diku.dk/torbenm/troll.msp
#count (sum 9d4) > (sum 6d6)