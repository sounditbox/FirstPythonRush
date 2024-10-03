import pickle


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


l1 = [1, 2, 3]

d = {'a': 1, 'b': l1}
c = MyClass(1, 2)
c2 = MyClass(3, 8)

pickle.dump(c, open('data1.pkl', 'wb'))
pickle.dump(c2, open('data2.pkl', 'wb'))
