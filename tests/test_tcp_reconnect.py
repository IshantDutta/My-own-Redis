
import socket

HOST = "127.0.0.1"
PORT = 6379


def test_connection(number):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(3)

    try:
        client.connect((HOST, PORT))
        print(f"Client {number}: Connected")

        client.sendall(b"PING\n")

        buffer = b""

        while b"\n" not in buffer:
            data = client.recv(1024)

            if not data:
                raise ConnectionError("Server disconnected")

            buffer += data

        response, remaining = buffer.split(b"\n", 1)

        print(f"Client {number}: {response.decode()}")

    finally:
        client.close()
        print(f"Client {number}: Disconnected")


if __name__ == "__main__":

    test_connection(1)
    test_connection(2)
    test_connection(3)

    print("\nReconnection test completed!")
