person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in person:
    print(f'{key}: {person[key]}')
print()

for key in person.keys():
    print(f'{key}: {person[key]}')
print()

for key, value in person.items():
    print(f'{key}: {value}')
print()
for value in person.values():
    print(f'{value}')
