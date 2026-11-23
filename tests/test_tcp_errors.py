
import socket

HOST = "127.0.0.1"
PORT = 6379


def receive_line(client):
    buffer = b""

    while b"\n" not in buffer:
        data = client.recv(1024)

        if not data:
            raise ConnectionError("Server disconnected")

        buffer += data

    message, remaining = buffer.split(b"\n", 1)
    return message.decode("utf-8")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    print("Connecting to server...")

    client.connect((HOST, PORT))

    print("Connected successfully!")

    client.sendall(b"\xff\n")
    print("Invalid UTF-8:", receive_line(client))

    client.sendall(b"\n")
    print("Empty command:", receive_line(client))

    client.sendall(b"PING\n")
    print("PING:", receive_line(client))

except (socket.timeout, ConnectionError, OSError) as error:
    print("TEST FAILED:", error)

finally:
    client.close()
    print("Test finished.")
