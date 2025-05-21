import math


class Circle:
    def set_radius(self, r):
        self.radius = r


class AreaCalculator(Circle):
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area


r = float(input("Enter the radius of the circle: "))

circle_area = AreaCalculator()
circle_area.set_radius(r)


print("Area of the circle is:", round(circle_area.calculate_area(), 2))
