import socket

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
filename = "file_to_send.txt"
try:
    with open(filename, "rb") as file:
        # Send filename first
        server_socket.sendto(filename.encode(), client_address)
        print(f"Filename sent: {filename}")
        
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
        
        print(f"File '{filename}' sent successfully in {chunk_number} chunks.")
except FileNotFoundError:
    print(f"File '{filename}' not found on server.")
    server_socket.sendto(b"FILE_NOT_FOUND", client_address)

# Close the socket
server_socket.close()