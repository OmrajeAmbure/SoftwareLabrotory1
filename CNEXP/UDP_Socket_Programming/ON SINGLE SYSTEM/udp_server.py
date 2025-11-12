# ==================== udp_server.py ====================
import socket
import os
import time

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
server_socket.bind(('0.0.0.0', 12345))  # Bind to all interfaces, port 12345
print("UDP Server is waiting for messages...")

# Task 1: Receive Message from Client
client_message, client_address = server_socket.recvfrom(1024)  # Receive message
print(f"Received from client {client_address}: {client_message.decode()}")

# Task 2: Send Response to Client
response = "Hello, Client! Message received successfully."
server_socket.sendto(response.encode(), client_address)
print(f"Response sent to client {client_address}")

# Task 3: File Transfer via UDP
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "file_to_send.txt")

try:
    with open(filename, "rb") as file:
        # Send filename first with newline delimiter
        filename_message = os.path.basename(filename) + "\n"
        server_socket.sendto(filename_message.encode(), client_address)
        print(f"Filename sent: {os.path.basename(filename)}")
        
        # Small delay to ensure filename is received separately
        time.sleep(0.1)
        
        # Read and send file data in chunks
        chunk_number = 0
        while True:
            file_data = file.read(1024)  # Read in chunks of 1024 bytes
            if not file_data:
                # Send end-of-file marker
                server_socket.sendto(b"EOF", client_address)
                break
            server_socket.sendto(file_data, client_address)
            chunk_number += 1
            time.sleep(0.01)  # Small delay between chunks to prevent packet loss
        
        print(f"File '{os.path.basename(filename)}' sent successfully in {chunk_number} chunks.")
except FileNotFoundError:
    print(f"File '{filename}' not found on server.")
    server_socket.sendto(b"FILE_NOT_FOUND", client_address)

# Close the socket
server_socket.close()