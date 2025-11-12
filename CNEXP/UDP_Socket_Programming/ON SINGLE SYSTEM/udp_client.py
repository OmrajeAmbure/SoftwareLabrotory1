# ==================== udp_client.py ====================
import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
server_address = ('localhost', 12345)  # Server's IP and port

# Task 1: Send Message to Server
message_to_server = "Hello, Server! This is a message from the UDP client."
client_socket.sendto(message_to_server.encode(), server_address)
print(f"Sent to server: {message_to_server}")

# Task 2: Receive Response from Server
response, server = client_socket.recvfrom(1024)
print(f"Received from server: {response.decode()}")

# Task 3: Receive File from Server
# Receive filename (with newline delimiter)
filename_data, server = client_socket.recvfrom(1024)
filename_received = filename_data.decode().strip()
print(f"Receiving file: {filename_received}")

# Check for error
if filename_received == "FILE_NOT_FOUND":
    print("File not found on server.")
else:
    received_filename = "received_file.txt"
    
    # Receive file data
    with open(received_filename, "wb") as file:
        while True:
            file_data, server = client_socket.recvfrom(1024)
            
            # Check for end-of-file marker
            if file_data == b"EOF":
                print(f"File '{received_filename}' received successfully.")
                break
            
            # Check for file not found error
            if file_data == b"FILE_NOT_FOUND":
                print("File not found on server.")
                break
            
            file.write(file_data)

# Close the socket
client_socket.close()