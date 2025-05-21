#print(dir(int))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 30)

print(p)


