from functools import reduce

a = [1, 2, 3, 4, 5]
mapped = map(lambda x: x * 2, a)
print(list(mapped))

b = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x % 2, b))
print(filtered)

c = [1, 2, 3, 4, 5]
reduced = reduce(lambda x, result: x * result, c, 42)
print(reduced)
