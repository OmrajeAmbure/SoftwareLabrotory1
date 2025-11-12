import socket

# Step 1: Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 2: Bind socket to address
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

print(f"UDP Server is running on {host}:{port}...")

# Step 3: Receive data from client
data, addr = server_socket.recvfrom(1024)
print("Received from client:", data.decode())

# Step 4: Send response back
server_socket.sendto("Hello UDP Client!".encode(), addr)

# Step 5: Close socket
server_socket.close()
