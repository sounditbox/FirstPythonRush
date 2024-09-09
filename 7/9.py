# Элемент строки является строкой единичной длины
# s = 'blahBlah bla you 123!@#'
# print(type(s))
# print(type(s[0]))
# print(type(s[1]))

# Преобразование строки
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# s = '     ljhtgh\t  \n '
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# Методы проверки
print('ya \t\n235624!#@%'.islower())
print('RGHTH!5 '.isupper())
print('khetrhдщшыоердш'.isalpha())
print('1346'.isdigit())
print('    \t\n'.isspace())
print('bukviand1234'.isalnum())

# Методы split и join
# split - разбивает строку на список строк по разделителю
# (по-умолчанию - пробельные символы)
print('  Мама\n  мыла  \tраму   рано   '.split())
print('Мама мыла раму'.split('а'))
print('Мама мыла раму'.split('мы'))
# join - Собирает список строк в строку по соединителю
print(''.join(['Мама', 'мыла', 'раму']))

# В единственной строке записаны целые числа через пробел. Найти их сумму
# => 1 2 3 4 5
# <= 15
print(sum(int(x) for x in input().split()))
