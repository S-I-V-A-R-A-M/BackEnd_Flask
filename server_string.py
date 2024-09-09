import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive data
data = conn.recv(1024)  # Adjust buffer size as needed
decoded_data = data.decode('utf-8')

# Assuming the data contains a string, int, and float (comma-separated)
str_data, int_data, float_data = decoded_data.split(',')
int_data = int(int_data)      # Convert string to integer
float_data = float(float_data)  # Convert string to float

print(f"Received: {str_data}, {int_data}, {float_data}")

conn.close()
server_socket.close()
