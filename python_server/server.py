
import socket

HOST = "127.0.0.1"
PORT = 6379

BUFFER_SIZE = 1024
MAX_MESSAGE_SIZE = 4096


def process_command(command):
    """Process a single client command."""

    command = command.strip()

    if not command:
        return "ERROR: Empty command"

    if command.upper() == "PING":
        return "PONG"

    elif command.upper() == "EXIT":
        return "GOODBYE"

    else:
        return "ERROR: Unknown command"


def handle_client(client_socket, client_address):
    """Handle communication with one connected client."""

    print(f"Client connected: {client_address}")

    buffer = b""

    try:
        while True:

            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                print("Client disconnected.")
                break

            buffer += data

            # Extract all complete messages
            while b"\n" in buffer:

                message, buffer = buffer.split(b"\n", 1)

                # Check message size
                if len(message) > MAX_MESSAGE_SIZE:
                    client_socket.sendall(
                        b"ERROR: Message too large\n"
                    )
                    return

                # Decode message safely
                try:
                    command = message.decode("utf-8")

                except UnicodeDecodeError:
                    client_socket.sendall(
                        b"ERROR: Invalid UTF-8\n"
                    )
                    continue

                print(f"Received: {command}")

                response = process_command(command)

                client_socket.sendall(
                    (response + "\n").encode("utf-8")
                )

            # Prevent unlimited incomplete message buffering
            if len(buffer) > MAX_MESSAGE_SIZE:
                client_socket.sendall(
                    b"ERROR: Message too large\n"
                )
                break

    except ConnectionResetError:
        print("Client connection was reset.")

    except OSError as error:
        print(f"Socket error: {error}")

    finally:
        client_socket.close()
        print(f"Client connection closed: {client_address}")


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))

    server.listen()

    print(f"Redis-like server running on {HOST}:{PORT}")
    print("Waiting for connections...")

    try:
        while True:

            client_socket, client_address = server.accept()

            handle_client(client_socket, client_address)

    except KeyboardInterrupt:
        print("\nShutting down server...")

    finally:
        server.close()
        print("Server stopped.")


if __name__ == "__main__":
    start_server()
