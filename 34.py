import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return "Это геометрическая фигура"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
circle = Circle(5)
rectangle = Rectangle(4, 6)


print(f"Площадь: {circle.area():.2f}")
print(f"Периметр: {circle.perimeter():.2f}")
print(circle.description())

print(f"Площадь: {rectangle.area()}")
print(f"Периметр: {rectangle.perimeter()}")
print(rectangle.description())