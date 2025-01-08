# int[] array = new int[5];

from sys import getsizeof

a = list()
for i in range(100):
    print(getsizeof(a))
    a.append(1)
