class Shape:  
    def set_values(self, base, height):
        self.base = base
        self.height = height

class Triangle(Shape):  
    def calculate_area(self):
        return 0.5 * self.base * self.height

class AreaDisplayer(Triangle):  
    def display(self):
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        self.set_values(b, h)
        area = self.calculate_area()
        print(f"Area of triangle: {round(area, 2)}")

obj = AreaDisplayer()
obj.display()
