
import socket

HOST = "127.0.0.1"
PORT = 6379

BUFFER_SIZE = 1024


def receive_message(client, buffer):
    """Read one complete newline-delimited response."""

    while b"\n" not in buffer:

        data = client.recv(BUFFER_SIZE)

        if not data:
            raise ConnectionError("Server disconnected")

        buffer += data

    message, buffer = buffer.split(b"\n", 1)

    return message.decode("utf-8"), buffer


def start_client():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    response_buffer = b""

    try:

        client.connect((HOST, PORT))

        print("Connected to our Redis server!")
        print("Type EXIT to quit.")

        while True:

            command = input("redis> ")

            if command.upper() == "EXIT":
                break

            # Send command
            message = command + "\n"

            client.sendall(message.encode("utf-8"))

            # Receive one complete response
            response, response_buffer = receive_message(
                client,
                response_buffer
            )

            print(response)

    except ConnectionError as error:
        print(f"Connection error: {error}")

    except OSError as error:
        print(f"Socket error: {error}")

    finally:
        client.close()
        print("Disconnected from server.")


if __name__ == "__main__":
    start_client()
