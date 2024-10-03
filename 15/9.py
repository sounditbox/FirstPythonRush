import pickle


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass({self.a}, {self.b})'


c = pickle.load(open('data1.pkl', 'rb'))
c2 = pickle.load(open('data2.pkl', 'rb'))
print(c)
print(c2)
