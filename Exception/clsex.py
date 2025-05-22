# Step 1: Define a custom exception
class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Step 2: Use it in a try-except block
try:
    raise MyError("This is a custom exception!")
except MyError as e:
    print("Caught custom exception:", e)
