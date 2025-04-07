import socket
import threading
import queue

def port_scan(target_host, port):
    """Scans a single port on the target host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout to avoid hanging
        result = sock.connect_ex((target_host, port))  # Non-blocking connect
        if result == 0:
            print(f"Port {port} is open on {target_host}")
        sock.close()
    except socket.error:
        pass  # Ignore socket errors

def worker(q):
    """Worker thread to scan ports from the queue."""
    while not q.empty():
        port = q.get()
        port_scan(target_host, port)
        q.task_done()

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    try:
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
    except ValueError:
        print("Invalid port range. Please enter integers.")
        exit()

    q = queue.Queue()

    # Populate the queue with ports to scan
    for port in range(start_port, end_port + 1):
        q.put(port)

    num_threads = 20  # You can adjust the number of threads

    # Create and start worker threads
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(q,))
        thread.daemon = True  # Allow the main program to exit even if threads are still running
        thread.start()

    q.join()  # Wait for all ports to be scanned
    print("Port scanning complete.")
