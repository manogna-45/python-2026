from functools import reduce
numbers = [2,5,10]
result = reduce(lambda x,y:x*y, numbers)
print(result)
