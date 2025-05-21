class Calculator:
    def set_data(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


calc = Calculator()
calc.set_data(num1, num2)


print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
