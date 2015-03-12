import time
tStart = time.time()

# generate number

num = 112668053
#1020304050607080900

while num < 100000000000:
    check = str(num**2)
    if str(num)[len(str(num))-1] == "3" or str(num)[len(str(num))-1] == "7":
        #print(check," = ",num,"^2")
        if check[2] =="2":
            print(check," = ",num,"^2")
        if len(check) == 17:
            #print(check," = ",num,"^2")
            if check[16] == "9":
                if check[14] == "8":
                    if check[12] == "7":
                        if check[10] == "6":
                            if check[8] == "5":
                                if check[6] == "4":
                                    if check[4] == "3":
                                        if check[2] == "2":
                                            print (num)
                                            break
        num = num+1
    else:
        num = num+1
        continue
    
#1389019170
print ("Run Time = " , str(time.time() - tStart))