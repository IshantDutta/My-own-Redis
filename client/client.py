
import socket

HOST = "127.0.0.1"
PORT = 6379

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to our server
client.connect((HOST, PORT))

print("Connected to our Redis server!")

# Send a command
command = "PING"
client.send(command.encode("utf-8"))

# Receive server response
response = client.recv(1024).decode("utf-8")

print("Server response:", response)

# Close connection
client.close()
