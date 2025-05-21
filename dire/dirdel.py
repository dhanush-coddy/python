import os

abc = input("Enter the Directory  name: ")

if not os.path.isfile(abc):
    os.rmdir(abc)
    print("Directory found and deleted.")
else:
    print("Directory not found.")
