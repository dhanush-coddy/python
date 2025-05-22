class InvalidMarkError(Exception):
    def __init__(self, mark):
        super().__init__(f" Error: {mark} is not a valid mark. Please enter a value between 0 and 100.")

try:
    mark = int(input("Enter your mark (0 to 100): "))

    if mark < 0 or mark > 100:
        raise InvalidMarkError(mark)
    elif mark > 35:
        print(" Result: Pass")
    else:
        print(" Result: Fail")

except InvalidMarkError as e:
    print(e)
except ValueError:
    print(" Error: Please enter a valid number (0–100 only).")
