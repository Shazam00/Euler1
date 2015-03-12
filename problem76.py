import time
tStart = time.time()

'''
def nway( total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0: count += 1    
    for amount in range( 0, total, c):
        count += nway(total - amount, coins)    
        #if amount % 10000 == 0:
        #    print ("%  --","  Current number: ", coins ," Time: ",str(time.time() - tStart))
    return count

target = 100 #100 , will take a really long time to find the solution :(
temp = []
for x in range(target-1):
    temp.append(x+1)
    print(x+1)
SetA = list(temp)
print (nway(target, SetA))
'''

ways = [0]*101
ways[0] = 1
count = 0
for i in range(1, len(ways)):
    for j in range(i, len(ways)):
        ways[j] += ways[j-i]
        count +=1
print ("solution: ",ways[100]-1)
print ("number of iterations: ",count)
print ("Run Time = " , str(time.time() - tStart))


#solution:  190569291
#number of iterations:  5050
#Run Time =  0.0019998550415039062
