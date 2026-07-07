def neon(n):
    sq = n*n 
    total = 0
    while sq > 0:
        digit = sq % 10
        total = total + digit
        sq = sq // 10
        
    return total == n
print(neon(9))
    
