from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle area =", 3.14 * r * r)

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Rectangle area =", l * b)

c = Circle()
r = Rectangle()

c.area()
r.area()