def armstrong(n):
    temp = n 
    total = 0
    while n>0:
        digits=n%10
        total= total+digits**3
        n=n//10
    return temp == total
print(armstrong(123))
