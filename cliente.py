import socket
import os
import urllib.request

def get_external_ip():
    try:
        with urllib.request.urlopen('https://api.ipify.org') as response:
            external_ip = response.read().decode('utf-8')
            return external_ip
    except Exception as e:
        print(f"Error fetching external IP: {e}")
        return None

def get_internal_ip():
    try:
        hostname = socket.gethostname()  # Obtener el nombre del host
        internal_ip = socket.gethostbyname(hostname)  # Obtener la IP interna
        return internal_ip
    except Exception as e:
        print(f"Error fetching internal IP: {e}")
        return None

def get_current_directory():
    try:
        current_dir = os.getcwd()  # Obtener el directorio actual
        return current_dir
    except Exception as e:
        print(f"Error fetching current directory: {e}")
        return None

def send_data_to_server(ip_data):
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect(('127.0.0.1', 5000))  # Conectar al servidor
        my_socket.send(ip_data.encode())  # Enviar datos al servidor
        # No imprimir los datos recibidos del servidor
        my_socket.close()  # Cerrar la conexión
    except Exception as e:
        print(f"Error sending data to server: {e}")

def start_http_server():
    try:
        os.system("python -m http.server 5000")  # Iniciar el servidor HTTP en el puerto 5000
    except Exception as e:
        print(f"Error starting HTTP server: {e}")

def main():
    external_ip = get_external_ip()
    internal_ip = get_internal_ip()
    current_dir = get_current_directory()

    if external_ip and internal_ip:
        ip_data = f"External IP: {external_ip}\nInternal IP: {internal_ip}\nCurrent Directory: {current_dir}"
        send_data_to_server(ip_data)
        start_http_server()

if __name__ == "__main__":
    main()
