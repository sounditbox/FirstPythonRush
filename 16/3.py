import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/42')
# Получение информации о статусе
print(response.status_code)  # Выводит статус код ответа
print(response.reason)  # Выводит текстовое описание статуса
print(response.ok)  # Возвращает True, если статус код меньше 400
# Получение заголовков
print(response.headers)  # Выводит заголовки ответа
print(response.headers['Content-Type'])
# Выводит значение конкретного заголовка
# Получение тела ответа
print(response.text)  # Выводит тело ответа в виде текста
print(response.json())  # Выводит тело ответа в виде JSON
print(response.content)  # Выводит тело ответа в виде байтов
