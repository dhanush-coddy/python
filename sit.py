class SIT: 
    def display(self):
        print("Welcome to School of Information Technology (SIT)")

class MCA(SIT):  
    def display(self):
        print("Welcome to MCA Department. Programming and Data Science!")

class MBA(SIT):  
    def display(self):
        print("Welcome to MBA Department. Business and Management Studies!")

class MSC(SIT):  
    def display(self):
        print("Welcome to MSC Department. Advanced Computing and Research!")


departments = [MCA(), MBA(), MSC()]

for dept in departments:
    dept.display()
