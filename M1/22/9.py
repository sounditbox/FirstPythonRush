def simple_hash(key, size):
    return sum(ord(char) for char in key) % size


def really_bad_hash(key, size):
    return 42


# Хеш-таблица с размером 5
size = 5
hash_table = [None] * size


# Хеширование ключей
def insert(table, key, value):
    index = simple_hash(key, size)
    if table[index] is None:
        table[index] = (key, value)
    else:
        print(
            f"Коллизия! Ключ '{key}' столкнулся с '{table[index][0]}' на индексе {index}")


insert(hash_table, "cerry", 50)
insert(hash_table, "banana", 30)  #
print(hash_table)
