# неизменяемые / изменяемые
from copy import deepcopy

a1 = [[1, 2], [3, 4]]
a2 = deepcopy(a1)

a1.append([5, 6])
a1[0].append(42)
print(a1, a2)
