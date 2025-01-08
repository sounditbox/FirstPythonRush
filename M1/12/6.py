# Наследование
# От общего к частному

class A:  # Родитель, надкласс, superclass
    def f(self):
        print('Hello')


class B(A):  # Наследник, подкласс, subclass
    pass


b = B()
b.f()
