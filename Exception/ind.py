#IndexError
try:
    names = ["Alice", "Bob", "Charlie"]
    i = int(input("Enter an index (0–2): "))
    print("Name:", names[i])
except IndexError:
    print("❌ Error: No name at that index.")
except ValueError:
    print("❌ Error: Please enter a number.")
