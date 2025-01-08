# Операции над множествами

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Пересечение
print(a & b)
print(a.intersection(b))
# Объединение
print(a | b)
print(a.union(b))
# Разность
print(a - b)
print(a.difference(b))
# Симметрическая разность
print(a ^ b)
print(a.symmetric_difference(b))
