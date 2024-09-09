
# a = b = c = 42
# print(a, b, c)

# (a, b, c) = (input(), 42, 'str')
# print(a, b, c)


*a, b, c = 1, 2, 3, 4, 5, 6, 7
print(a, b, c)
firstname, *middle_names, surname = 'Elizabeth Alexandra Mary Windsor'.split()
print(firstname, middle_names, surname)
