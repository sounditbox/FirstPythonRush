class Animal:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @staticmethod
    def staticMethod():
        print('static method')

    def eat(self):
        print('eating')

    def sleep(self):
        print('sleeping')


class Dog(Animal):
    def bark(self):
        print('barking')

    def eat(self):
        print('eating a bone')


Animal.staticMethod()
Dog.staticMethod()

d = Dog('Fido', 3)
d.staticMethod()
d.eat()
d.sleep()
d.bark()
# print(d._name)
# print(d._Animal__age)
