import http.client

# Настройки прокси-сервера
proxy_host = '10.10.1.10'
proxy_port = 3128

# Целевой URL
dest_url = 'httpbin.org'
dest_path = '/ip'

# Создаем соединение с прокси-сервером
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Устанавливаем туннель к целевому серверу
conn.set_tunnel(dest_url)

# Отправляем GET-запрос
conn.request('GET', dest_path)
# Получаем ответ
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode('utf-8'))
# Закрываем соединение
conn.close()
