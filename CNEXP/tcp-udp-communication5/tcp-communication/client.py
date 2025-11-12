import socket

# Step 1: Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to server
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# Step 3: Send message to server
message = "Hello Server, I am TCP Client!"
client_socket.send(message.encode())

# Step 4: Receive response from server
data = client_socket.recv(1024).decode()
print("Server says:", data)

# Step 5: Close connection
client_socket.close()
