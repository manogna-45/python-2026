class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")
class Circle(Shape):
    def area(self):
        print("Circle Area")

r1 = Rectangle()
c1 = Circle()
r1.area()
c1.area()
