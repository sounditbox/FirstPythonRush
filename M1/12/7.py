from math import pi


class Shape:
    def info(self):
        return f'{self.__class__.__name__}: S:{self.square()}, P:{self.perimeter()}'

    def square(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def square(self):
        return self.r ** 2 * pi

    def perimeter(self):
        return 2 * (self.r * pi)


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"


class RegularPolygon:
    def __init__(self, n, l):
        self.n = n
        self.l = l

    def perimeter(self):
        return self.n * self.l


class Square(RegularPolygon, Rectangle):
    def __init__(self, a):
        RegularPolygon.__init__(self, 4, a)

    def __str__(self):
        return f'Square({self.a})'


shapes = [Square(10), Rectangle(10, 15), Rectangle(14, 65), Circle(5), Shape()]
for shape in shapes:
    print(shape.info())

# MRO - Method Resolution Order - линеаризация

