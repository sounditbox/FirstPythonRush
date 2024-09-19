

# 9
# Реализуйте функцию group_by_key(items, key_func),
# которая принимает список элементов items
# и функцию key_func, которая определяет ключ для каждого элемента.
# Функция должна вернуть словарь, где ключи — это результаты key_func,
# а значения — списки элементов, соответствующие этим ключам
def group_by_key(items, key_func):
    pass


items = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']


def first_letter(s):
    return s[0]


print(group_by_key(items, first_letter))
# Вывод: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}






