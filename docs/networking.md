
# Networking Fundamentals

## 1. Introduction

The networking layer allows clients to communicate with our Redis-like server.

We use TCP (Transmission Control Protocol) for reliable communication between the client and server.

## 2. TCP Socket Programming

The Python socket module provides the networking interface.

Our server uses:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Where:

- AF_INET specifies IPv4.
- SOCK_STREAM specifies TCP.

## 3. Server Socket Lifecycle

The server follows these operations:

| Function | Purpose |
|---|---|
| socket() | Creates a socket |
| bind() | Assigns IP address and port |
| listen() | Waits for incoming connections |
| accept() | Accepts a client |
| recv() | Receives bytes |
| sendall() | Sends all supplied bytes |
| close() | Closes the socket |

## 4. Client Socket Lifecycle

The client:

1. Creates a TCP socket.
2. Connects to the server.
3. Encodes commands into bytes.
4. Sends commands.
5. Receives responses.
6. Closes the connection.

## 5. TCP Byte Streams

TCP provides a continuous stream of bytes.

It does not preserve application-level message boundaries.

For example, a client may send:

```text
PING
PING
```

The server might receive both commands together or in separate chunks.

Similarly, one command can arrive in multiple chunks.

## 6. Message Framing

To identify complete commands, we implemented newline-based message framing.

Example:

```text
PING\n
SET name Noor\n
GET name\n
```

The server maintains a byte buffer.

Incoming data is appended to the buffer until a newline is found.

Complete messages are extracted while incomplete messages remain in the buffer.

## 7. Error Handling

The networking implementation includes:

- Invalid UTF-8 detection.
- Empty command detection.
- Unknown command handling.
- Maximum message size enforcement.
- Connection reset handling.
- Socket error handling.
- Client disconnection detection.

## 8. Message Size Protection

The current maximum message size is 4096 bytes.

Messages exceeding this limit are rejected.

The server uses a receive buffer of 1024 bytes.

These are separate concepts:

- Receive buffer: How many bytes are requested in one recv() call.
- Maximum message size: Maximum accepted application message size.

## 9. Current Networking Limitations

- Clients are handled sequentially.
- The current protocol uses newline delimiters.
- The client and server use a simple request-response pattern.
- Concurrent clients are planned for a later development phase.

## 10. Future Networking Improvements

- Implement RESP.
- Support multiple concurrent clients.
- Introduce thread-based client handling.
- Improve protocol validation.
- Implement more robust client response buffering.
