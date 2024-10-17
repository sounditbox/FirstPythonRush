import requests

# URL для запроса
url = 'https://api.ipify.org?format=json'

# Словарь с настройками прокси
proxies = {
    'http': 'http://1.20.203.29:8081',
    'https': 'https://198.24.187.93:8001'
}
# Отправка GET-запроса через прокси
response = requests.get(url, proxies=proxies)
# Вывод полученного IP-адреса
print(response.json())
