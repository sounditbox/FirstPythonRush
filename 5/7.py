l1 = [1, 2, 3]
l2 = [4, 5, 6]
# Конкатенация списков
print(l1 + l2)
print(l2 + l1)
# Дублирование
print(l1 * 3)

for i in range(len(l1)):
    elem = l1[i]
    elem *= 2
print(l1)