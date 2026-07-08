def strong(n):
    temp = n 
    total = 0
    while n>0:
        digit = n%10
        fact = 1
        for i in range(1,digit+1):
            fact = fact*i 
        total+=fact
        n//10
    return temp == total
print(strong(145))
    
