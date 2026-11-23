
import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 6379

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP address and port
server.bind((HOST, PORT))

# Start listening for incoming connections
server.listen()

print(f"Redis-like server running on {HOST}:{PORT}")
print("Waiting for connections...")

# Accept a client connection
client_socket, client_address = server.accept()

print(f"Client connected: {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode("utf-8")

print(f"Received: {data}")

# Send response
if data.strip().upper() == "PING":
    client_socket.send("PONG".encode("utf-8"))
else:
    client_socket.send("ERROR: Unknown command".encode("utf-8"))

# Close connection
client_socket.close()
server.close()
