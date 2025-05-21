class Shape:
    def display(self):
        print("This is a shape.")

class Circle(Shape):
    def display(self):
        print("This is a circle. Area = πr²")

class Square(Shape):
    def display(self):
        print("This is a square. Area = side²")

class Triangle(Shape):
    def display(self):
        print("This is a triangle. Area = ½ × base × height")


shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.display()
