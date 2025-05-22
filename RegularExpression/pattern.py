import re

text = "helloxhelloxhello"

pattern = r"[0-9]"

abv = re.findall(pattern, text)
if abv:
    print("findall(): successful")
else:
    print("findall(): failed")
print(abv)