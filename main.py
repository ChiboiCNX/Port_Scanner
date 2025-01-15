import socket
import sys 
from datetime import datetime
import pyfiglet
from threading import Thread, Lock


script_title = pyfiglet.figlet_format("Port Scanner")
print(script_title)


if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:    
        print("Error: Invalid hostname. please enter a valid target")
        sys.exit(1)
else:
    print("Usage: python main.py <target>")
    sys.exit(1)
   
print("-" * 45)
print(f"Scan Target: {target}")    
print(f"Scanning started : {datetime.now()}")
print("-" * 45)

print_lock = Lock()

def scan_port(port):
    try:
       scan_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.setdefaulttimeout(1)
       result = scan_sockets.connect_ex((target, port))
       if result == 0:
        with print_lock:
            print(f"Port {port} is open")
        scan_sockets.close()
    except socket.error:
        pass

threads = []
try:
    for port in range(1, 10000):
        thread = Thread(target = scan_port, args = (port,))   
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  

except KeyboardInterrupt:
    print("Scan stopped by user!!")
    sys.exit(1) 

print("-" * 45)
print(f"scanning completed: {datetime.now()}")     
print("-" * 45)                 



