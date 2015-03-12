#Euler 205
'''
I saved probabilities to obtain each total for each player. 
Then I just had to combine those totals. 
The algorithm is O(sides1^dices1 + sides2^dices2 + (max_total^2)/2) so there are 6^6 + 4^9 + (36^2)/2 = 309448 iterations running in 0.46 seconds in Python. 
'''

# 6 6-sided dices
colin = [0] * 37
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        t = a + b + c + d + e + f
                        colin[t] += 1
 
# 9 4-sided dices
peter = [0] * 37
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    t = a + b + c + d + e + f + g + h + i
                                    peter[t] += 1
for i in range(37):
    colin[i] /= float(6**6)
    peter[i] /= float(4**9)
 
s = 0.0
for ipeter in range(37):
    for icolin in range(ipeter):
        s += peter[ipeter] * colin[icolin]
 
s = round(s * 10000000) / 10000000
print (s)