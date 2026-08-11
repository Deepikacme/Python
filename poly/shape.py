class Shape:
    def area(self):
        print("Calculating Area")
class Rectangle(Shape):
    def area(self):
        length=10
        breadth=5
        print("Area of Rectangle =",length*breadth)
class Circle(Shape):
    def area(self):
        radius=7
        print("Area of Circle =",3.14*radius*radius)
class Triangle(Shape):
    def area(self):
        base=8
        height=6
        print("Area of Triangle =",0.5*base*height)
r=Rectangle()
c=Circle()
t=Triangle()
r.area()
c.area()
t.area()