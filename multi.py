class Circle:
    def set_circle_radius(self, radius):
        self.radius = radius

    def get_circle_area(self):
        return 3.14 * self.radius ** 2

class Square:
    def set_square_side(self, side):
        self.side = side

    def get_square_area(self):
        return self.side ** 2


class AreaCalculator(Circle, Square):
    def display_area(self):
        choice = input("Enter shape (circle/square): ").strip().lower()
        
        if choice == "circle":
            r = float(input("Enter radius: "))
            self.set_circle_radius(r)
            area = self.get_circle_area()
            print(f"Area of the circle: {round(area, 2)}")

        elif choice == "square":
            s = float(input("Enter side: "))
            self.set_square_side(s)
            area = self.get_square_area()
            print(f"Area of the square: {round(area, 2)}")

        else:
            print("Invalid shape entered.")


obj = AreaCalculator()
obj.display_area()
