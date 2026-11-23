
import socket

HOST = "127.0.0.1"
PORT = 6379
BUFFER_SIZE = 1024


def process_command(command):
    """Process a single client command."""

    command = command.strip()

    if command.upper() == "PING":
        return "PONG"

    elif command.upper() == "EXIT":
        return "GOODBYE"

    else:
        return "ERROR: Unknown command"


def handle_client(client_socket, client_address):
    """Handle communication with one connected client."""

    print(f"Client connected: {client_address}")

    # Buffer stores incoming bytes
    buffer = b""

    try:
        while True:

            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                print("Client disconnected.")
                break

            # Add incoming bytes to our buffer
            buffer += data

            # Process complete messages
            while b"\n" in buffer:

                message, buffer = buffer.split(b"\n", 1)

                command = message.decode("utf-8")

                print(f"Received: {command}")

                response = process_command(command)

                # Send response with newline delimiter
                client_socket.sendall(
                    (response + "\n").encode("utf-8")
                )

    except ConnectionError:
        print("Connection error.")

    except UnicodeDecodeError:
        print("Invalid text encoding.")

    finally:
        client_socket.close()
        print("Client connection closed.")


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
