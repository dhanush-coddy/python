class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other): return Calculator(self.value + other.value)
    def __sub__(self, other): return Calculator(self.value - other.value)
    def __mul__(self, other): return Calculator(self.value * other.value)
    def __truediv__(self, other): return Calculator(self.value / other.value) if other.value != 0 else "Cannot divide by zero"
    def __str__(self): return f"{self.value}"


#  Input and usage in fewer lines
a = Calculator(int(input("Enter first number: ")))
b = Calculator(int(input("Enter second number: ")))

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
