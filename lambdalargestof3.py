largest = lambda a,b,c: a if a>b and a>c else b if b>a and b>c else c 
print(largest(10,20,30))