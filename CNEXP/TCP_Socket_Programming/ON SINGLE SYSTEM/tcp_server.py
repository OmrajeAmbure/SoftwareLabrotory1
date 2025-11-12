# ==================== tcp_server.py ====================
import socket
import os

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
server_socket.bind(('0.0.0.0', 12345))  # Bind to all interfaces, port 12345
server_socket.listen(1)  # Listen for incoming connections
print("Server is waiting for a connection...")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Task 1: Receive Message from Client
client_message = client_socket.recv(1024).decode()
print(f"Received from client: {client_message}")

# Task 2: Send Response to Client
response = "Hello, Client! Message received successfully."
client_socket.send(response.encode())
print(f"Response sent to client {client_address}")

# Task 3: File Transfer via TCP
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "file_to_send.txt")

try:
    with open(filename, "rb") as file:
        # Send filename first with a delimiter
        filename_message = os.path.basename(filename) + "\n"
        client_socket.send(filename_message.encode())
        print(f"Filename sent: {os.path.basename(filename)}")
        
        # Small delay to ensure filename is received separately
        import time
        time.sleep(0.1)
        
        # Read and send file data
        file_data = file.read()
        client_socket.send(file_data)
        
        print(f"File '{os.path.basename(filename)}' sent successfully.")
except FileNotFoundError:
    print(f"File '{filename}' not found on server.")
    error_message = "FILE_NOT_FOUND\n"
    client_socket.send(error_message.encode())

# Close the sockets
client_socket.close()
server_socket.close()
