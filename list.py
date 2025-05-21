man=['z','b','c','b',1,2,3,4]
print(man)
xan=[1,2,3,4,5,6,7,8,9]
print(xan)
lan=['a','d','v','b']
print(lan)


nest=[[1,2,3,4,5,6,7,8,9],['a','d','v','b'],['z','b','c','b',1,2,3,4]]
print(nest)

print(nest[1])

#append()
lan.append('f')
print(lan)

#insert()
lan.insert(3,'r')
print(lan)

#extend()
man.extend([10,19,39])
print(man)

#remove()
man.remove(2)
print(man)

#pop()
man.pop(2)
print(man)

#clear()
man.clear()
print(man)

#slice
print(xan[4:9])

#update
xan[4]=1000
print(xan)

#concatination
print(xan+lan)

print(nest*3)
print(man,lan,xan,nest)

print(4 in man)

unord=[5,3,9,0,274,3,5,4,3,45,5,7]

print(sorted(unord))
unord.reverse()
print(unord)

# Using len() to find the total number of elements
length = len(unord)
print(f"Length of the list: {length}")

# Using count() to find how many times the number 5 appears
count_5 = unord.count(5)
print(f"Number 5 appears {count_5} times")

# Example: count occurrences of another number
count_3 = unord.count(3)
print(f"Number 3 appears {count_3} times")

xyz=[1,4,8,6,9,4,7,58,3,85]
for i in xyz:
    print(i)