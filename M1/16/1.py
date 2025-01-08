import json

# Создание Python-объекта (словаря)
users = [
    {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    },
    {
        'name': 'Bob',
        'age': 33,
        'city': 'Paris'
    }
]
# Сериализация в JSON
# json_string = json.dumps(data)
# print(json_string)
# Запись в файл

with open('data.json', 'w') as f:
    json.dump(users, f, indent=4, sort_keys=True)

# Чтение из файла
with open('data.json', 'r') as f:
    data_from_file = json.load(f)
    print(data_from_file)
# Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Десериализация строки JSON

json_string = '{"name": "Bob", "age": 25}'
users = json.loads(json_string)
print(users)  # Вывод: {'name': 'Bob', 'age': 25}
