import datetime
import socket

# Создаем сокет TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем сокет к адресу и порту
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
# Начинаем прослушивание
server_socket.listen()
print(f"Сервер слушает на {host}:{port}")

messages = ['Добро пожаловать в чатик']
client_socket = None
while True:
    # Принимаем соединение
    if not client_socket:
        client_socket, addr = server_socket.accept()
        print(f"Подключение от {addr}")

    client_socket.sendall('\n'.join(messages).encode())

    # Получаем данные от клиента
    mes = client_socket.recv(1024).decode()
    mes_dt = datetime.datetime.now().strftime('%H:%M %D.%m')
    messages.append(f'{mes}\t{mes_dt}')
    print(messages)

# # Закрываем соединение
# client_socket.close()
