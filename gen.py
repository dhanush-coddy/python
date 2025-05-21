def count_x(max):
    count = 1
    while count <= max:
        yield (count, count**2)
        count += 1

num = count_x(10)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
