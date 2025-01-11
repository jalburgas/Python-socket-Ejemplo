import socket

def start_server():
    try:
        # Crear un socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asociar el socket a una dirección IP y puerto
        server_socket.bind(('0.0.0.0', 5000))

        # Escuchar conexiones entrantes
        server_socket.listen(1)
        print("Esperando conexiones en el puerto 5000...")

        # Aceptar una conexión
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada desde {client_address}")

        # Recibir el nombre del cliente
        client_name = client_socket.recv(1024).decode()
        print(f"Nombre del cliente: {client_name}")

        # Enviar un mensaje de saludo al cliente
        what_to_send = f'Hello {client_name}'
        client_socket.send(what_to_send.encode())

        # Cerrar la conexión
        client_socket.close()
        server_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_server()

   

   

