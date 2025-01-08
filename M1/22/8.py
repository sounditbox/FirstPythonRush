def simple_hash(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)  # ord() возвращает числовое значение символа
    return hash_value % 10  # возвращаем остаток от деления на 10


print(simple_hash("apple"))
print(simple_hash("bananb"))