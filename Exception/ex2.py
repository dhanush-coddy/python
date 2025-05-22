# Custom exception class
class NegativeNumberError(Exception):
    def __init__(self, number):
        super().__init__(f" Error: {number} is a negative number. Please enter a positive number.")

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(" Thank you! You entered a positive number:", num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print(" Error: Please enter a valid number (not letters or symbols).")
