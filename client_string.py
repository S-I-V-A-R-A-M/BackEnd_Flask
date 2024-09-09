import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Prepare data to send (string, integer, float)
str_data = "Hello"
int_data = 42
float_data = 3.14

# Format data as a string and encode it
message = f"{str_data},{int_data},{float_data}"
client_socket.send(message.encode('utf-8'))

client_socket.close()
