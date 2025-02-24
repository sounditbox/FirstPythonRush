# Используем базовый образ Ubuntu
FROM ubuntu:20.04
# Устанавливаем Python
RUN apt-get update && apt-get install -y python3
# Копируем файлы приложения в контейнер
COPY . /app
# Устанавливаем рабочую директорию
WORKDIR /app
# Указываем команду для запуска приложения
CMD ["python3", "app.py"]