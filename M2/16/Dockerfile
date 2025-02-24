# Базовый образ
FROM python:3.10
# Установка рабочей директории
WORKDIR /app
# Копирование файлов
COPY requirements.txt .
RUN pip install -r requirements.txt \
COPY . .
# Запуск приложения
CMD ["python", "app.py"]