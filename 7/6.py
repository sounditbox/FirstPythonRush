s = {'syrsyj', 'dtuyjgh', 'ru8k57k', 'zbnujgfc'}
# Удаление:
s.discard(42)
print(s)
# s.remove(42) - KeyError, если нет такого значения
print(s)
rand_elem = s.pop()  # Удаляет и возвращает случайный элемент
print(s, rand_elem)

