import requests

try:
    response = requests.get(
        'https://api.github.com/users/spu')  # Несуществующий пользователь
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err}")
except Exception as err:
    print(f"Произошла другая ошибка: {err}")
else:
    print("Запрос выполнен успешно!")
