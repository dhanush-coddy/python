class Student:
    def set_data(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")


s1 = Student()
s2 = Student()
s1.set_data("Bob", 102)
s2.set_data("mobob", 103)
s1.display()
s2.display()