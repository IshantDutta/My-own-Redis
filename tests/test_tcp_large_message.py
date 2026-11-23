
import socket

HOST = "127.0.0.1"
PORT = 6379

client = socket.create_connection((HOST, PORT))
client.settimeout(3)

try:
    # Send a message larger than 4096 bytes
    message = b"A" * 5000 + b"\n"

    client.sendall(message)

    response = client.recv(1024)

    print("Server response:", response.decode().strip())

finally:
    client.close()
