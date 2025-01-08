# 8
# Напишите функцию calculate(operation, initial_value, *args), где:
# operation — функция, принимающая два аргумента,
# initial_value — начальное значение,
# а *args — произвольное количество числовых аргументов.
# Функция должна последовательно применять операцию ко всем аргументам,
# начиная с initial_value.
def calculate(operation, initial_value, *args):
    pass


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(calculate(add, 0, 1, 2, 3, 4))  # Вывод: 10 (0+1+2+3+4)
print(calculate(multiply, 1, 1, 2, 3, 4))  # Вывод: 24 (1*1*2*3*4)


