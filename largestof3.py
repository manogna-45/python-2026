def largestof3(a,b,c):
    if a >= b and a>=c:
        return a 
    elif b>=a and b>=c:
        return b
    else:
        return c 
print(largestof3(10,8,20))
