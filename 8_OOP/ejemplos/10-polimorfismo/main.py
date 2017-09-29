 import math

 class Circle:
     def __init__(self, diameter):
         self.diameter = diameter

     @property
     def radius(self):
         return self.diameter / 2

     @classmethod
     def form_radius(cls, radius):
         return cls(radius * 2)


 class Square:
     def __init__(self, side):
         self.side = side


 class AreaCalculator:
     @staticmethod
     def calculate_area(shapes):
         result = 0
         for shape in shapes:
             shape_area = 0
             if isinstance(shape, Circle):
                 shape_area = (shape.radius ** 2) * math.pi
             if isinstance(shape, Square):
                 shape_area = shape.side ** 2
             result += shape_area
         return result


 circles = [
     Circle(10),
     Circle(30),
     Square(40)
 ]

 print(AreaCalculator.calculate_area(circles))

########################################################################

# import math
#
# class Circle:
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#     @property
#     def radius(self):
#         return self.diameter / 2
#
#     @classmethod
#     def form_radius(cls, radius):
#         return cls(radius * 2)
#
#     def get_area(self):
#         return (self.radius ** 2) * math.pi
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def get_area(self):
#         return self.side ** 2
#
# class Triangle():
#     def __init__(self, side):
#         self.side = side
#
#
# class AreaCalculator:
#     @staticmethod
#     def calculate_area(shapes):
#         result = 0
#         for shape in shapes:
#             result += shape.get_area()
#         return result
#
#
# circles = [
#     Circle(10),
#     Circle(30),
#     Square(40),
#     Triangle(40)
# ]
#
# print(AreaCalculator.calculate_area(circles))

########################################################################

## Resuelto con EAFP
# import math
#
# class Circle:
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#     @property
#     def radius(self):
#         return self.diameter / 2
#
#     @classmethod
#     def form_radius(cls, radius):
#         return cls(radius * 2)
#
#     def get_area(self):
#         return (self.radius ** 2) * math.pi
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def get_area(self):
#         return self.side ** 2
#
#
# class Triangle():
#     def __init__(self, side):
#         self.side = side
#
#
# class AreaCalculator:
#     @staticmethod
#     def calculate_area(shapes):
#         result = 0
#         for shape in shapes:
#             try:
#                 result += shape.get_area()
#             except AttributeError:
#                 continue
#         return result
#
# circles = [
#     Circle(10),
#     Circle(30),
#     Square(40),
#     Triangle(40)
# ]
#
# print(AreaCalculator.calculate_area(circles))

########################################################################

# import math
#
# class Shape:
#     def get_area(self):
#         #pass
#         raise ValueError('get_area method no implemented')
#
# class Circle(Shape):
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#     @property
#     def radius(self):
#         return self.diameter / 2
#
#     @classmethod
#     def form_radius(cls, radius):
#         return cls(radius * 2)
#
#     def get_area(self):
#         return (self.radius ** 2) * math.pi
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def get_area(self):
#         return self.side ** 2
#
#
# class Triangle(Shape):
#     def __init__(self, side):
#         self.side = side
#
#
# class AreaCalculator:
#     @staticmethod
#     def calculate_area(shapes):
#         result = 0
#         for shape in shapes:
#             if isinstance(shape, Shape):
#                 result += shape.get_area()
#         return result
#
# shapes = [
#     Circle(10),
#     Circle(30),
#     Square(40),
#     Triangle(40)
# ]
#
# print(AreaCalculator.calculate_area(shapes))


########################################################################

# Resuelto con Abstract Base Clases

import math
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @classmethod
    def form_radius(cls, radius):
        return cls(radius * 2)

    def get_area(self):
        return (self.radius ** 2) * math.pi


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 3

class AreaCalculator:
    @staticmethod
    def calculate_area(shapes):
        result = 0
        for shape in shapes:
            if isinstance(shape, Shape):
                result += shape.get_area()
        return result

shapes = [
    Circle(10),
    Circle(30),
    Square(40),
    Triangle(40)
]

print(AreaCalculator.calculate_area(shapes))
