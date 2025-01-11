import socket
import os
import urllib.request

def get_external_ip():
    try:
        # Abrir una URL para obtener la dirección IP externa
        with urllib.request.urlopen('https://api.ipify.org') as response:
            external_ip = response.read().decode('utf-8')  # Leer y decodificar la respuesta
            return external_ip
    except Exception as e:
        # Imprimir el error si ocurre un problema al obtener la IP externa
        print(f"Error fetching external IP: {e}")
        return None

def get_internal_ip():
    try:
        hostname = socket.gethostname()  # Obtener el nombre del host
        internal_ip = socket.gethostbyname(hostname)  # Obtener la IP interna del host
        return internal_ip
    except Exception as e:
        # Imprimir el error si ocurre un problema al obtener la IP interna
        print(f"Error fetching internal IP: {e}")
        return None

def get_current_directory():
    try:
        current_dir = os.getcwd()  # Obtener el directorio actual de trabajo
        return current_dir
    except Exception as e:
        # Imprimir el error si ocurre un problema al obtener el directorio actual
        print(f"Error fetching current directory: {e}")
        return None

def send_data_to_server(ip_data):
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket TCP/IP
        my_socket.connect(('127.0.0.1', 5000))  # Conectar al servidor en el puerto 5000
        my_socket.send(ip_data.encode())  # Enviar los datos IP al servidor
        # No imprimir los datos recibidos del servidor
        my_socket.close()  # Cerrar la conexión del socket
    except Exception as e:
        # Imprimir el error si ocurre un problema al enviar los datos al servidor
        print(f"Error sending data to server: {e}")

def start_http_server():
    try:
        os.system("python -m http.server 5000")  # Iniciar un servidor HTTP en el puerto 5000
    except Exception as e:
        # Imprimir el error si ocurre un problema al iniciar el servidor HTTP
        print(f"Error starting HTTP server: {e}")

def main():
    external_ip = get_external_ip()  # Obtener la IP externa
    internal_ip = get_internal_ip()  # Obtener la IP interna
    current_dir = get_current_directory()  # Obtener el directorio actual

    if external_ip and internal_ip:
        # Preparar los datos IP en un formato legible
        ip_data = f"External IP: {external_ip}\nInternal IP: {internal_ip}\nCurrent Directory: {current_dir}"
        send_data_to_server(ip_data)  # Enviar los datos al servidor
        start_http_server()  # Iniciar el servidor HTTP

if __name__ == "__main__":
    main()  # Ejecutar la función principal
