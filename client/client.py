import socket

HOST = "127.0.0.1"
PORT = 6379


def start_client():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect((HOST, PORT))

    print("Connected to our Redis server!")
    print("Type PING to test or EXIT to quit.")

    try:
        while True:

            command = input("redis> ")

            if command.upper() == "EXIT":
                break

            # Send command with newline delimiter
            message = command + "\n"

            client.sendall(message.encode("utf-8"))

            # Receive response until newline
            response_buffer = b""

            while b"\n" not in response_buffer:
                data = client.recv(1024)

                if not data:
                    print("Server disconnected.")
                    return

                response_buffer += data

            response, remaining = response_buffer.split(b"\n", 1)

            print(response.decode("utf-8"))

    finally:
        client.close()
        print("Disconnected from server.")


if __name__ == "__main__":
    start_client()
