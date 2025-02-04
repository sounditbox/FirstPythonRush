import socket
# Создаем сокет TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаемся к серверу
host = 'localhost'
port = 12345
client_socket.connect((host, port))


while True:
    # Получаем ответ от сервера
    data = client_socket.recv(1024).decode()
    print(f"Получено от сервера:\n{data}")

    # Отправляем данные на сервер
    message = input('Введите сообщение:')
    client_socket.sendall(message.encode())
    # Закрываем соединение
# client_socket.close()
