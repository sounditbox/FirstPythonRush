def my_print(*args, sep=' ', end='\n'):
    print(sep.join([str(i) for i in args]) + end)


my_print(1, 2, 3)
my_print(1, 2, 3, end='?', sep='!')
my_print(1, 2, 3, sep='!')
my_print(1, 2, 3, end='?')

# print('.'.join(['127', '0', '0', '1']))
