a = 'абв'
b = 'abc'
# print(a < b)

# Unicode
# ord(sym) - возвращает порядковый номер символа в Unicode
# chr(ind) - возвращает символ в Unicode под номером ind
# for i in range(1000, 1130):
#     print(f'i: {i}, chr: {chr(i)} ')
# print(chr(128534))
# print('😖')
# print('\U0001F616')
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end='')
