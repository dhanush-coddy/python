#ValueError   
try:
    str = int("abc")  # This will raise a ValueError
    print(str)
except ValueError:
    print("❌ Error: Cannot convert 'abc' to an integer.")
