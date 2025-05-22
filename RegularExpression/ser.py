import re

text = "Python is powerful and popular."
match = re.search(r'powerful', text)

if match:
    print("Match:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())
else:
    print("No match found")
