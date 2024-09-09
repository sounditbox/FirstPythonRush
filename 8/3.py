# get

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


person2 = {
    "name": "Mike",
    "age": 28,
    "city": "London",
    'country': 'UK'
}

users = [person, person2]

for u in users:
    print(u.get('country', 'Default_country'))
