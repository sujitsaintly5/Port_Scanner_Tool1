import socket
import threading
import queue
import time

def port_scan(target_host, port, open_ports, closed_ports):
    """Scans a single port on the target host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"[{time.strftime('%H:%M:%S')}] Port {port} is open on {target_host}")
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()
    except socket.error:
        pass

def worker(q, target_host, open_ports, closed_ports):
    """Worker thread to scan ports from the queue."""
    while not q.empty():
        port = q.get()
        port_scan(target_host, port, open_ports, closed_ports)
        q.task_done()

if __name__ == "__main__":
    target_host = input("Enter the target host IP address: ") # Explicitly ask for IP address
    try:
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
    except ValueError:
        print("Invalid port range. Please enter integers.")
        exit()

    q = queue.Queue()
    open_ports = []
    closed_ports = []

    for port in range(start_port, end_port + 1):
        q.put(port)

    num_threads = 20

    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(q, target_host, open_ports, closed_ports))
        thread.daemon = True
        thread.start()

    q.join()

    print("\n--- Scan Summary ---")
    print(f"Target: {target_host}")
    print(f"Total Ports Scanned: {end_port - start_port + 1}")
    print(f"Open Ports: {len(open_ports)}")
    print(f"Closed Ports: {len(closed_ports)}")

    if open_ports:
        print("\nOpen Ports:")
        print(open_ports)
