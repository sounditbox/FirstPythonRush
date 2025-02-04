# 6
# Напишите функцию custom_filter(func, *args),
# которая принимает функцию func и произвольное количество аргументов.
# Функция должна вернуть список тех аргументов, для которых func(arg) возвращает True.
#
def is_even(n):
    return n % 2 == 0


def custom_filter(func, *args):
    pass


print(custom_filter(is_even, 1, 2, 3, 4, 5, 6))  # Вывод: [2, 4, 6]



