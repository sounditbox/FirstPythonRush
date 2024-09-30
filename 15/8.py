import pickle


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


l1 = [1, 2, 3]

d = {'a': 1, 'b': l1}
c = MyClass(1, 2)
c2 = MyClass(3, 8)

pickle.dump(d, open('data.txt', 'wb'))