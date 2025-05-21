def areaofcircle(func):
    def wrapper():
        r = int(input("Enter radius of circle: "))
        area = 3.14 * r * r
      
        func(area)  
        
    return wrapper

@areaofcircle
def grate(area):
    print(f"The area of the circle is: {area}")

grate()
