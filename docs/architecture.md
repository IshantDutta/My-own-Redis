
# System Architecture

## 1. Project Overview

Build Your Own Redis is a miniature Redis-inspired in-memory database developed from scratch.

The project aims to understand database internals, networking, data structures, memory management and systems programming.

The initial implementation is being developed in Python, followed by a low-level implementation in C.

## 2. Current Architecture

The current implementation follows a basic client-server architecture.

```text
+-------------------+
|   Python Client   |
|    client.py      |
+---------+---------+
          |
          | TCP Connection
          |
          v
+-------------------+
|    TCP Server     |
|     server.py     |
+---------+---------+
          |
          v
+-------------------+
|  Message Buffer   |
|                   |
| Newline Framing   |
+---------+---------+
          |
          v
+-------------------+
| Command Processor |
|                   |
| PING              |
| EXIT              |
| Unknown Commands  |
+---------+---------+
          |
          v
+-------------------+
| Response Generator|
+-------------------+
```

## 3. Communication Flow

1. The client creates a TCP socket.
2. The client connects to the server.
3. The server accepts the connection.
4. The client sends a command.
5. The server receives bytes.
6. Incoming bytes are stored in a buffer.
7. Complete messages are extracted using newline delimiters.
8. The command processor generates a response.
9. The server sends the response to the client.
10. The connection closes when the client disconnects.

## 4. Network Configuration

| Property | Value |
|---|---|
| Protocol | TCP |
| IP Address | 127.0.0.1 |
| Port | 6379 |
| Address Family | IPv4 |
| Socket Type | SOCK_STREAM |
| Message Framing | Newline Delimited |
| Maximum Message Size | 4096 bytes |
| Receive Buffer | 1024 bytes |

## 5. Current Limitations

- The server handles clients sequentially.
- The database engine has not yet been implemented.
- Only basic commands are supported.
- The current communication format is temporary.
- Data is not persisted to disk.
- Concurrent client handling is not implemented.

## 6. Future Architecture

The planned architecture will include:

- RESP protocol parser and serializer.
- Command dispatcher.
- In-memory hash table.
- Strings, Lists, Sets and Hashes.
- Expiration manager.
- Persistence manager.
- Concurrent client handling.
- C implementation using Winsock.

## 7. Technology Stack

- Python
- C
- TCP/IP
- Python Socket API
- Winsock
- GCC / MinGW
- Git and GitHub
- pytest
