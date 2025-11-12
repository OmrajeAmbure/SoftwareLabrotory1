import socket

# Step 1: Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to host and port
host = '127.0.0.1'   # localhost
port = 12345
server_socket.bind((host, port))

# Step 3: Listen for client connections
server_socket.listen(1)
print(f"Server is listening on {host}:{port}...")

# Step 4: Accept a connection
conn, addr = server_socket.accept()
print("Connected by:", addr)

# Step 5: Receive data from client
data = conn.recv(1024).decode()
print("Client says:", data)

# Step 6: Send a response
conn.send("Message received successfully!".encode())

# Step 7: Close connection
conn.close()
