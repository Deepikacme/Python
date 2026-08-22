from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        print("Shape: Rectangle")

class Rectangle(Shape):
    def area(self):
        print("Area:", 10 * 5)

obj = Rectangle()
obj.area()
obj.display_shape()