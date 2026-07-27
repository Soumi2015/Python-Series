class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle =", round(area, 2))

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print("Perimeter of Circle =", round(perimeter, 2))

c1 = Circle(5)
c1.area()
c1.perimeter()                