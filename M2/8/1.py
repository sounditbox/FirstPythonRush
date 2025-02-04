class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


p1 = Person("John", 30)
Person.__init__(p1, 'John', 30)
p1.greet()
p2 = Person("Jane", 25)
print(dir(p1))

d = {'name': 'John', 'age': 30}
print(d.keys())
print(d.values())
print(d.items())
