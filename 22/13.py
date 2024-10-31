class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dummy = []

    #
    def __hash__(self):
        return hash(self.x) + hash(self.y)


vectors = {}
v = Vector2d(1, 1)
vectors[v] = 42
print(vectors)
v.x = 42
v.dummy.append(123)
vectors[v] = 420
print(vectors)
