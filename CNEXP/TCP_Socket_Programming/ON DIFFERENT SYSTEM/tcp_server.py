import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Listening on all interfaces, port 12345
server_socket.listen(1)  # Listen for incoming connections

# Get and display server's IP address
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)
print(f"Server is running on IP: {server_ip}, Port: 12345")
print("Server is waiting for a connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Task 1: Receive Message from Client
client_message = client_socket.recv(1024).decode()  # Receive message from client
print(f"Received from client: {client_message}")

# Task 2: Send Response to Client
client_socket.sendall("Hello, Client! Message received successfully.".encode())

# Task 3: File Transfer
filename = "file_to_send.txt"
try:
    with open(filename, "rb") as file:
        file_data = file.read(1024)  # Read in chunks of 1024 bytes
        while file_data:
            client_socket.send(file_data)  # Send file data to the client
            file_data = file.read(1024)
    print(f"File '{filename}' sent successfully.")
except FileNotFoundError:
    print(f"File '{filename}' not found on server.")

# Close the connection
client_socket.close()
server_socket.close()
print("Connection closed.")