from functools import reduce

numbers = [12, 45, 67, 23, 89, 34]

product = reduce(lambda x, y: x * y, numbers)    

print("Greatest number is:", product)