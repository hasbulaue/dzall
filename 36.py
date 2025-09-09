
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения...")
    
    conn, addr = server_socket.accept()
    print(f"Подключен клиент: {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Получено от клиента: {data}")
        response = f"Ответ сервера на: {data}"
        conn.send(response.encode())
    
    conn.close()

if __name__ == "__main__":
    start_server()