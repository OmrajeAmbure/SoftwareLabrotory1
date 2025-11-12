import socket

# Step 1: Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 2: Send data to server
host = '127.0.0.1'
port = 12345
message = "Hello Server, I am UDP Client!"
client_socket.sendto(message.encode(), (host, port))

# Step 3: Receive response
data, server = client_socket.recvfrom(1024)
print("Server says:", data.decode())

# Step 4: Close socket
client_socket.close()
