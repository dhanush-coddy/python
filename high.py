import math

class Shape:
    def get_input(self, shape_type):
        if shape_type == "circle":
            r = float(input("Enter radius of the circle: "))
            return r
        elif shape_type == "square":
            s = float(input("Enter side of the square: "))
            return s
        else:
            return None


class Circle(Shape):
    def calculate_area(self):
        radius = self.get_input("circle")
        area = math.pi * radius ** 2
        print(f"Area of the circle: {round(area, 2)}")


class Square(Shape):
    def calculate_area(self):
        side = self.get_input("square")
        area = side ** 2
        print(f"Area of the square: {round(area, 2)}")


shape_choice = input("Choose shape (circle/square): ").strip().lower()

if shape_choice == "circle":
    obj = Circle()
    obj.calculate_area()

elif shape_choice == "square":
    obj = Square()
    obj.calculate_area()

else:
    print("Invalid shape choice.")
