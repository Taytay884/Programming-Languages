##### Questions & Answers #####
# - How many functions in minimal functions?
# 15 functions.
# - How many functions in minimal lines of code without empty lines?
# 17 functions, 98 lines
# - There's a difference between a program with minimal lines of codes than a minimal number of functions?
# Yes, minimal number of functions - Many lines of code. Less lines - more functions.
# the less functions you use the more lines of code you will have!
# - Can we convert one of the functions to Static? 
# Yes, we converted areaByHeronFormula into a static method!
##### Questions & Answers #####

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def print_info(self):
        print("Shape:", type(self).__name__)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def print_info(self):
        super().print_info()
        print("Radius:", self.radius)

class Polygonal(Shape):
    def __init__(self, lengths):
        self.lengths = lengths

    def perimeter(self):
        return sum(self.lengths)

    @abstractmethod
    def area(self):
        pass

    def print_info(self):
        super().print_info()
        print("Side Lengths:", self.lengths)

class Triangle(Polygonal):
    def __init__(self, side1, side2, base):
        super().__init__([side1, side2, base])

    def area(self):
        a, b, c = self.lengths
        return self.areaByHeronFormula(a, b, c)

    @staticmethod
    def areaByHeronFormula(a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Quadrangle(Polygonal):
    def __init__(self, side1, side2, side3, side4):
        super().__init__([side1, side2, side3, side4])

class Square(Quadrangle):
    def __init__(self, length):
        super().__init__(length, length, length, length)

    def area(self):
        return self.lengths[0] ** 2

class Rhombus(Quadrangle):
    def __init__(self, length, diagonalH, diagonalV):
        super().__init__(length, length, length, length)
        self.diagonalH = diagonalH
        self.diagonalV = diagonalV

    def area(self):
        return 0.5 * self.diagonalH * self.diagonalV

    def print_info(self):
        super().print_info()
        print("DiagonalH:", self.diagonalH)
        print("DiagonalV:", self.diagonalV)

class Kite(Quadrangle):
    def __init__(self, length1, length2, diagonalH, diagonalV):
        super().__init__(length1, length1, length2, length2)
        self.diagonalH = diagonalH
        self.diagonalV = diagonalV

    def area(self):
        return 0.5 * self.diagonalH * self.diagonalV

    def print_info(self):
        super().print_info()
        print("DiagonalH:", self.diagonalH)
        print("DiagonalV:", self.diagonalV)

class Trapeze(Quadrangle):
    def __init__(self, side1, side2, base1, base2, height):
        super().__init__(side1, side2, base1, base2)
        self.side1 = side1
        self.side2 = side2
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def print_info(self):
        super().print_info()
        print("Height:", self.height)

class Pentagon(Polygonal):
    def __init__(self, side1, side2, side3, side4, side5):
        super().__init__([side1, side2, side3, side4, side5])

    @abstractmethod
    def area(self):
        pass

class RegularPolygon(Polygonal):
    def __init__(self, sidesNumber, length):
        super().__init__([length] * sidesNumber)
        self.sidesNumber = sidesNumber
        self.length = length

    @abstractmethod
    def area(self):
        pass

class EquilateralTriangleFromRegularPolygon(RegularPolygon):
    def __init__(self, length):
        super().__init__(3, length)

    def area(self):
        return Triangle.areaByHeronFormula(self.length, self.length, self.length)

class SquareFromRegularPolygon(RegularPolygon):
    def __init__(self, length):
        super().__init__(4, length)

    def area(self):
        return self.length ** 2

## Tests!

# Create a Circle with radius 5
circle = Circle(5)
circle.print_info()

# Create a Triangle with sides 3, 4, and 5
triangle = Triangle(3, 4, 5)
triangle.print_info()

# Create a Square with side length 6
square = Square(6)
square.print_info()

# Create a Rhombus with side length 4 and diagonals 6 and 8
rhombus = Rhombus(4, 6, 8)
rhombus.print_info()

# Create a Kite with side lengths 3, 3, 5, and 5 and diagonals 6 and 8
kite = Kite(3, 5, 6, 8)
kite.print_info()

# Create a Trapeze with side lengths 3, 4, bases 6 and 8, and height 5
trapeze = Trapeze(3, 4, 6, 8, 5)
trapeze.print_info()

# Create an Equilateral Triangle from Regular Polygon with side length 7
equilateral_triangle = EquilateralTriangleFromRegularPolygon(7)
equilateral_triangle.print_info()

# Create a Square from Regular Polygon with side length 8
square_from_regular_polygon = SquareFromRegularPolygon(8)
square_from_regular_polygon.print_info()
