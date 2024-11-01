import socket
import os
import urllib.request

with urllib.request.urlopen('https://api.ipify.org') as response:
    external_ip = response.read().decode('utf-8')

hostname = socket.gethostname()  # Nombre del host
internal_ip = socket.gethostbyname(hostname)  # IP interna
current_dir = os.getcwd()  # Directorio actual

#print(f"IP interna: {internal_ip}")
#print(f"IP pública: {external_ip}")
#print(f"Directorio actual: {current_dir}")
#print(f"Nombre del host: {hostname}")

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 5000))  # IP del servidor

# Enviar datos al servidor
my_socket.send(external_ip.encode()+internal_ip.encode())

data = my_socket.recv(1024)  # Recibir datos del servidor
#print(data.decode())

# Iniciar un servidor HTTP en el puerto 5000
os.system("python -m http.server 5000")

#my_socket.close()
