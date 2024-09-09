person = {"name": "Alice", "age": 25, "city": "New York"}
value_to_find = 26
if value_to_find in person.values():
    print(f"Значение {value_to_find} присутствует в словаре.")
else:
    print(f"Значение {value_to_find} отсутствует в словаре.")
