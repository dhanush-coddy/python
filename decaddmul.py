def add_and_multiply(func):
    def wrapper(n):
        add_result = n + n
        mul_result = n * n
        return func(add_result, mul_result)
    return wrapper

@add_and_multiply
def show_results(add, mul):
    print(f"Addition result: {add}")
    print(f"Multiplication result: {mul}")


show_results(5)
