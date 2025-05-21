def decorator(func):
    def wrapper():
        mesg = input("Enter your name: ")
        print("hello")
        func(mesg)  
        print("goodmorning")
    return wrapper

@decorator
def grate(mesg):  
    print(mesg)

grate()

