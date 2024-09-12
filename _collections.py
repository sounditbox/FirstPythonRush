# len(col) - количество элементов col
# val in col - проверяет, есть ли val в col

# all(col) - Проверяет, что все элементы True
# any(col) - Проверяет, что хотя бы элемент True

a = 42, True, 'blabla', 0.01, ''
print(all(a))
a = 0, False, '', 0.0, 'False'
print(any(a))

# ordered - str, list, tuple
# col[i] - получить элемент под индексом i
# col[start:stop:step] - взятие среза
# .index()
# .count()

# mutable - list, set, dict
# Можно добавлять, удалять и изменять элементы




# list - mutable ordered multitype iterable
# tuple - immutable ordered multitype iterable
# str - immutable ordered monotype iterable
# set - mutable unordered multitype iterable (unique immutable elements)
# dict - mutable unordered multitype iterable (elements - pairs key:value,
# where keys are unique immutable)
