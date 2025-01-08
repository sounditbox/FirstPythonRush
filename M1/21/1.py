# Элементарные операции:
# - + * / // %
# = == > < >= <=
# a = 1
from time import time

n = 1000

start = time()
counter = 0  # 1 операция
inner_counter = 0
# Внешний цикл
for i in range(n):  # 1 операция и n итераций
    counter = counter + 1
    # Внутренний цикл
    for j in range(n):
        inner_counter += 1
end = time()
print(f'time: {end - start}')
print(counter, inner_counter)