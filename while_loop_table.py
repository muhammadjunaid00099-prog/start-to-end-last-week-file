num = 1

while num <= 10:
    print("Table of", num)
    
    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1
    
    print("--------------------")
    num += 1
    

for num in range(1, 11):
    print("Table of", num)
    
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    
    print("--------------------")