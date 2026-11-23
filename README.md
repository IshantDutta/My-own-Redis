# Build MY Own Redis

A miniature Redis-inspired in-memory database built from scratch using Python and C.

## About

This project aims to recreate the fundamental concepts behind Redis rather than simply using an existing Redis implementation.

The goal is to understand how an in-memory database works internally, including networking, data structures, command processing, memory management, concurrency and persistence.

## Current Development Status

**Phase 1: Foundations — In Progress**

Implemented so far:

- Basic TCP server and client.
- Persistent server operation.
- Newline-based message framing.
- Multiple commands over one connection.
- Fragmented message handling.
- Invalid UTF-8 detection.
- Empty command handling.
- Unknown command handling.
- Maximum message size protection.
- Client disconnection handling.
- Graceful server shutdown.

## Technology Stack

- Python
- C
- TCP/IP and socket programming
- MinGW GCC
- Winsock
- pytest
- Git and GitHub

## Project Structure

```text
build-your-own-redis/
│
├── python_server/
│   ├── server.py
│   ├── client_handler.py
│   ├── command_parser.py
│   ├── database.py
│   ├── data_structures.py
│   ├── resp.py
│   ├── persistence.py
│   └── expiration.py
│
├── c_server/
│   ├── src/
│   └── include/
│
├── client/
│   ├── client.py
│   └── README.md
│
├── tests/
├── benchmarks/
├── docs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Running the Current Python Server

### 1. Clone the repository

```bash
git clone https://github.com/IshantDutta/My-own-Redis
cd build-your-own-redis
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the server

```bash
python python_server/server.py
```

### 6. Start the client in another terminal

```bash
python client/client.py
```

## Current Supported Commands

| Command | Description |
|---|---|
| PING | Tests server connectivity |
| EXIT | Exits the client |
| Unknown commands | Returns an error |

## Development Roadmap

1. Foundations and TCP networking.
2. In-memory database engine and hash tables.
3. Redis Serialization Protocol (RESP).
4. Strings, Lists, Sets and Hashes.
5. Concurrent clients, expiration and persistence.
6. C implementation using Winsock.
7. Testing and performance benchmarking.
8. Documentation and GitHub publication.

## Learning Objectives

This project explores:

- Data Structures and Algorithms
- Computer Networks
- TCP/IP and Socket Programming
- Operating Systems
- Memory Management
- Database Internals
- Concurrent Programming
- File I/O
- System Design

## Disclaimer

This is an educational project inspired by Redis. It is not a production-ready replacement for Redis.

The implementation is developed incrementally for learning and experimentation.

## License

MIT License (to be added when the project is ready for publication).
