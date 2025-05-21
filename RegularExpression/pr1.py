import re

text = input("Enter a string: ")
p = input("Enter a substring or pattern: ")

# 1. re.match() — only matches at the beginning
abv = re.match(p, text)
if abv:
    print("match(): successful")
else:
    print("match(): failed")

# 2. re.search() — searches the whole string
abv = re.search(p, text)
if abv:
    print("search(): successful")
else:
    print("search(): failed")

# 3. re.findall() — returns all matching substrings
abv = re.findall(p, text)
if abv:
    print("findall(): successful")
else:
    print("findall(): failed")
