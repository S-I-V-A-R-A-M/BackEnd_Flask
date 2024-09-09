import socket
import json

# Setup the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Prepare a dictionary to send
data_dict = {"name": "John", "age": 30, "height": 5.8}

# Serialize the dictionary to JSON and send it
json_data = json.dumps(data_dict)
client_socket.send(json_data.encode('utf-8'))

client_socket.close()
