# import my_module
# my_module.f()
# print(my_module.const)
# a = my_module.A()
from my_package.my_module import f as func, const, A


def f():
    print('Bye')


func()
print(const)
a = A()
