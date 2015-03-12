import time
#from fractions import gcd
tStart = time.time()

def gcd(a,b):
    #Euclid's Algorithm
    while b:
        a, b = b, a % b
    return a 

def totient(n):
    tot, pos = 0, n-1
    while pos>0:
        if gcd(pos,n)==1: tot += 1
        pos -= 1
    return tot 

count = 0
size = 100
'''
current = 2
while current <= size:
    count = count + totient(current)
    print (current, " ", count)
    current = current + 1
'''
'''
current = 1000000
while current >= 2:
    count = count + totient(current)
    print (current, " ", count)
    current = current - 1
'''

'''
for d in range(2, size+1):
    count = count + totient(d)
    print (d, " ", count)
'''
'''
for d in range(2, size+1):
    for n in range(1, d+1):
        if gcd(n,d) == 1:
            temp = n/d
            count = count + 1
    print (d, " ", count)
'''
L = 1000000 + 1
phi = range(L)
for n in range(2, L):
    if phi[n] == n:
        for k in range(n, L, n):
            phi[k] = phi[k] *  (n - 1.)/n;
 
print ("Answer to PE72 =", int(sum(phi)-1))

# sum (phi(n)) for n=2 to 1000000

print (count)
print ("Run Time = " , str(time.time() - tStart))
