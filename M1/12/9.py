class A:
    def __init__(self):
        self.public = 42
        self._protected = 84
        self.__private = 168


a = A()
a._protected = 42
a.__private = 42
print(a.__private)
