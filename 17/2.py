import requests

# Отправляем GET-запрос
response = requests.get('https://api.github.com/users/defunkt')
# Проверяем статус ответа
print(response.status_code)  # Например, 200
print(response.reason)  # Например, 'OK'
# Получаем заголовки
# print(response.headers)
# print(response.headers['Content-Type'])
# Получаем тип содержимого ответа
# Получаем тело ответа
# print(response.text)  # Получаем текст ответа
data = response.json()
# Преобразуем ответ в JSON и получаем словарь данных
print(data['name'])  # Выводим имя пользователя
# Проверка на успешный ответ
if response.ok:
    print("Запрос выполнен успешно")
else:
    print("Произошла ошибка:", response.status_code)
