# ==================== tcp_client.py ====================
import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
server_address = ('localhost', 12345)  # Server's IP and port

# Connect to the server
client_socket.connect(server_address)
print(f"Connected to server at {server_address}")

# Task 1: Send Message to Server
message_to_server = "Hello, Server! This is a message from the client."
client_socket.send(message_to_server.encode())
print(f"Sent to server: {message_to_server}")

# Task 2: Receive Response from Server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Task 3: Receive File from Server
# Receive filename first (with newline delimiter)
filename_data = client_socket.recv(1024).decode().strip()
print(f"Receiving file: {filename_data}")

# Check for error
if filename_data == "FILE_NOT_FOUND":
    print("File not found on server.")
else:
    received_filename = "received_file.txt"
    
    # Receive file data
    with open(received_filename, "wb") as file:
        file_data = client_socket.recv(4096)  # Receive file content
        file.write(file_data)
    
    print(f"File '{received_filename}' received successfully.")

# Close the socket
client_socket.close()