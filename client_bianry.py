import socket

# Setup the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Open an image file in binary mode and send its content
with open('image.jpg', 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.send(data)

print("File sent.")
client_socket.close()
