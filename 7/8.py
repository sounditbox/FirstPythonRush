# Суперсила множеств:
# Проверка вхождения элемента во множество выполняется моментально

from datetime import datetime

a = [bool(i) for i in range(10 ** 9)]
s = set(a)
start = datetime.now()
-1 in a
end = datetime.now()
print(end - start)

start = datetime.now()
-1 in s
end = datetime.now()
print(end - start)
