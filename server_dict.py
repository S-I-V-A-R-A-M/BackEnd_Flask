import socket
import json

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive data
data = conn.recv(1024)
decoded_data = data.decode('utf-8')

# Deserialize JSON back to dictionary
received_dict = json.loads(decoded_data)
print(f"Received dictionary: {received_dict}")

conn.close()
server_socket.close()
