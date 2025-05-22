import re

text = input("Enter password \n")
result = re.sub(r'\d', '*', text)
print(result)
