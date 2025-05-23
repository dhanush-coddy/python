numbers = list(range(1, 51))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x ** 2, even_numbers))

print("Squares of even numbers from 1 to 50:")
print(squares)
