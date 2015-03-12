sum = 1
spiral = 1
while spiral < 1001:
    spiral += 2
    sum+=spiral**2
    sum+=spiral**2 - (spiral-1)
    sum+=spiral**2 - (spiral-1)*2
    sum+=spiral**2 - (spiral-1)*3
print(sum)