
import socket

HOST = "127.0.0.1"
PORT = 6379

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    client.connect((HOST, PORT))

    print("Connected to server")

    # Send two commands together
    client.sendall(b"PING\nPING\n")

    # Collect responses until two complete lines arrive
    buffer = b""

    while buffer.count(b"\n") < 2:
        data = client.recv(1024)

        if not data:
            raise ConnectionError("Server disconnected")

        buffer += data

    responses = buffer.split(b"\n")

    print("Raw response:", repr(buffer))
    print("First response:", responses[0].decode())
    print("Second response:", responses[1].decode())

finally:
    client.close()
