import requests
# Замените 'YOUR_API_KEY' на ваш реальный API ключ
api_key = 'YOUR_API_KEY'
city = 'Moscow'
# Формируем URL запроса
url =
f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=
{api_key}&units=metric'
# Отправляем запрос и получаем ответ
response = requests.get(url)
# Парсим ответ
if response.status_code == 200:
 data = response.json()
 weather = data['weather'][0]['description']
 temperature = data['main']['temp']
 print(f"В городе {city} сейчас: {weather}, температура:
{temperature}°C")
else:
 print("Ошибка при получении данных о погоде.")
