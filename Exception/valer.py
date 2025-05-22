try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
#ZeroDivisionError
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")

except ValueError:
    print("❌ Error: Please enter valid numbers.")

finally:
    print("✅ Program finished.")