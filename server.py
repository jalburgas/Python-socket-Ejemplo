import socket
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 5050))
server_socket.listen(1)
(client_socket, client_address) = server_socket.accept()
client_name = client_socket.recv(1024)
what_to_send = 'Hello ' + client_name.decode()
client_socket.send(what_to_send.encode())
client_socket.close()
server_socket.close()
    
   

   
