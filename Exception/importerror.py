try:
    from random import randint
    print("Random number:", randint(1, 10))
except ImportError as e:
    print("Import failed:", e)
