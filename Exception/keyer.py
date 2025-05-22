#KeyError
try:
    student = {"name": "John", "grade": "A"}
    key = input("Enter the key to look up (name/grade): ")
    print("Value:", student[key])
except KeyError:
    print("❌ Error: That key doesn't exist.")
