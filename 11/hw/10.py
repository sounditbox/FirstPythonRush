# 10
# Создайте функцию apply_functions(value, *functions),
# которая принимает начальное значение и произвольное количество функций.
# Функция должна последовательно применять каждую функцию к значению
# и возвращать итоговый результат.

def apply_functions(value, *functions):
    pass


def increment(x):
    return x + 1


def square(x):
    return x * x


print(apply_functions(2, increment, square))  # Вывод: 9 ((2 + 1)^2)
