# Вводятся два целых числа. Вывести их по возрастанию через пробел

a, b = int(input()), int(input())
if a > b:
    a, b = b, a  # swap
print(a, b)