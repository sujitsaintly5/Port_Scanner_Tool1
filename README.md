# 🔍 Multi-threaded Port Scanner

A simple Python script for performing a basic multi-threaded TCP port scan on a target host using the `socket`, `threading`, and `queue` libraries.

## 📦 Imports

- **`socket`**: Enables network operations such as creating sockets and connecting to hosts.
- **`threading`**: Supports concurrent execution of tasks, allowing multiple ports to be scanned simultaneously.
- **`queue`**: Provides a thread-safe queue to coordinate port scanning among multiple threads.

## ⚙️ How It Works

### `port_scan` Function

- Takes a `target_host` and `port` as input.
- Creates a TCP socket (`AF_INET` for IPv4, `SOCK_STREAM` for TCP).
- Sets a timeout of 1 second to avoid hanging.
- Attempts to connect to the target port using `connect_ex`.
- Prints the port number if it is open.
- Handles any socket-related errors gracefully.

### `worker` Function

- Continuously pulls port numbers from the queue.
- Calls `port_scan` for each port.
- Uses `q.task_done()` to indicate task completion.

### Main Block (`if __name__ == "__main__":`)

- Accepts user input for target host and port range.
- Validates inputs.
- Creates a queue and fills it with the specified range of ports.
- Spawns 20 worker threads (customizable).
- Waits for all tasks to complete with `q.join()`.

## 🚀 How to Run

1. Save the code as `port_scanner.py`.
2. Open your terminal or command prompt.
3. Run the script: `** python port_scanner.py**`
4. It will ask for Host address 

   ```bash
   python port_scanner.py
