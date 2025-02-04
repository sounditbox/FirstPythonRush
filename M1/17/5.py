import http.client
import json

# Данные для отправки
data = {
    "title": "foo",
    "body": "bar",
    "userId": 42
}
payload = json.dumps(data)
# Заголовки
headers = {
    'Content-Type': 'application/json'
}
# Создание подключения
with http.client.HTTPSConnection("jsonplaceholder.typicode.com") as conn:
    # Отправка POST-запроса
    conn.request("POST", "/posts", body=payload, headers=headers)
    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)
    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

