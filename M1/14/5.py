class Vector2d(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # +
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2d(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __or__(self, other):  # |
        pass

    def __and__(self, other):  # &
        pass

    def __contains__(self, item): # in
        pass

    def __repr__(self):
        return f'Vector2d({self.x}, {self.y})'


v1 = Vector2d(5, 5)
v2 = Vector2d(3, 4)
v3 = v1 + v2
# exec() - execute - выполняет код, записаный в строке
print(v3)