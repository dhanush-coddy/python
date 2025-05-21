import os

abc = input("Enter the file name: ")

if os.path.isfile(abc):
    os.remove(abc)
    print("File found and deleted.")
else:
    print("File not found.")
