<h2>Explaination</h2>
<br>
<h3>Imports</h3>

<h4>1. socket:</h4> This library is essential for network operations. It allows us to create sockets, connect to hosts, and send/receive data.
threading: This library provides support for creating and managing threads, enabling concurrent execution of the port_scan function.
queue: This library is used to create a thread-safe queue, which is crucial for coordinating the work of multiple threads. The queue holds the list of ports to be 
scanned.

<h4>2. port_scan Function</h4>

This function takes the target_host and port as input.
It creates a socket using socket.socket(socket.AF_INET, socket.SOCK_STREAM) (AF_INET for IPv4, SOCK_STREAM for TCP).
sock.settimeout(1) sets a timeout of 1 second for the connection attempt. This prevents the program from hanging if a port doesn't respond.
sock.connect_ex((target_host, port)) attempts to establish a connection. connect_ex is used because it returns an error code instead of raising an exception, making it easier to handle connection failures.
If result is 0, it means the connection was successful, and the port is open.
sock.close() closes the socket.
The try...except socket.error block is used to handle potential socket errors (e.g., if the host is unreachable).

<h4>3. worker Function</h4>

This function is executed by each thread.
It takes a queue object (q) as input.
The while not q.empty(): loop continues as long as there are ports in the queue.
port = q.get() retrieves a port number from the queue.
port_scan(target_host, port) calls the port_scan function to scan the retrieved port.
q.task_done() signals to the queue that the processing of the port is complete. This is important for the q.join() method.
if __name__ == "__main__": Block

This block ensures that the code inside it is executed only when the script is run directly (not when it's imported as a module).
It prompts the user to enter the target_host, start_port, and end_port.
It uses a try...except ValueError block to handle cases where the user enters invalid port numbers.
q = queue.Queue() creates a queue object.
The for loop populates the queue with the range of ports to be scanned.
num_threads = 20 sets the number of threads to be created. You can adjust this number to control the speed of the scan. A higher number of threads can make the scan faster, but be cautious not to overwhelm the target host.
The next for loop creates and starts the worker threads.
thread = threading.Thread(target=worker, args=(q,)) creates a new thread that will execute the worker function, passing the queue as an argument.
thread.daemon = True sets the thread as a daemon thread. This means that the thread will be terminated when the main program exits, even if it has not finished its task. This is generally a good practice for worker threads.
thread.start() starts the thread.
q.join() blocks until all items in the queue have been processed. This ensures that the main program waits for all ports to be scanned before printing the "Port scanning complete" message.
How to Run the Code

Save the code as a Python file (e.g., port\_scanner.py).
Open a terminal or command prompt.
Run the script using python port_scanner.py.
The program will prompt you to enter the target host and the range of ports to scan.
Important Considerations

Ethical Use: Use this tool responsibly and ethically. Unauthorized port scanning is illegal and can have serious consequences. Only scan hosts that you have explicit permission to scan.
Firewalls and Intrusion Detection Systems (IDS): Be aware that your port scans might be detected by firewalls and IDS. Excessive or aggressive scanning can lead to your IP address being blocked.
Error Handling: The code includes basic error handling, but you can enhance it to handle more specific exceptions and provide more informative error messages.
Scan Types: This code performs a basic TCP connect scan. There are other types of port scans (e.g., SYN scan, UDP scan) that provide different information and have different characteristics.
Root Privileges: On some systems, certain types of scans might require root privileges.
Rate Limiting: You might want to implement rate limiting to avoid overwhelming the target host and to be less likely to be detected. You can use time.sleep() to introduce delays between scans.
This multi-threaded port scanner provides a good foundation. Remember to use it responsibly and ethically, and you can further expand its functionality as needed!
