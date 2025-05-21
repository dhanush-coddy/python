xyz = [1, 2, 3, 4, 5, 6, 3, 8, 9, 7, 0]

even = []
odd = []


for i in xyz:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("Even numbers:", even)
print("Total even numbers:", len(even))


print("Odd numbers:", odd)
print("Total odd numbers:", len(odd))

print(sum(xyz))
