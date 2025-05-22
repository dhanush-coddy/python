from functools import reduce

numbers = [12, 45, 67, 23, 89, 34]

greatest = reduce(lambda a, b: a if a > b else b, numbers)

print("Greatest number is:", greatest)
