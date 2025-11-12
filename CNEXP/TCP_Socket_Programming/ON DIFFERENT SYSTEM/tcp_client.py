import socket

# IMPORTANT: Replace 'SERVER_IP_ADDRESS' with the actual IP address of your server
SERVER_IP = 'SERVER_IP_ADDRESS'  # e.g., '192.168.1.100' or '10.0.0.5'
SERVER_PORT = 12345

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Attempting to connect to server at {SERVER_IP}:{SERVER_PORT}...")
try:
    client_socket.connect((SERVER_IP, SERVER_PORT))  # Connect to the server's IP and port
    print("Successfully connected to server!")
except Exception as e:
    print(f"Failed to connect to server: {e}")
    exit(1)

# Task 1: Send Message to Server
message_to_server = "Hello, Server! This is a message from the client."
client_socket.sendall(message_to_server.encode())  # Send message to server
print(f"Sent to server: {message_to_server}")

# Task 2: Receive Response from Server
response = client_socket.recv(1024).decode()  # Receive response from server
print(f"Received from server: {response}")

# Task 3: Receive and Save the File from Server
filename = "received_file.txt"
with open(filename, "wb") as file:
    file_data = client_socket.recv(1024)  # Receive file data in chunks
    while file_data:
        file.write(file_data)
        file_data = client_socket.recv(1024)
print(f"File '{filename}' received successfully.")

# Close the connection
client_socket.close()
print("Connection closed.")