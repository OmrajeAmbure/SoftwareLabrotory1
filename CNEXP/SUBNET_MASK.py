import ipaddress

# Input IP network from user
ip = input("Enter the network (e.g., 192.168.1.0/24): ")

# Create IP network object
net = ipaddress.ip_network(ip, strict=False)

# Display network details
print("\nNetwork Address :", net.network_address)
print("Broadcast Address :", net.broadcast_address)
print("Subnet Mask :", net.netmask)
print("Number of Hosts :", net.num_addresses - 2)
print("Available IP Range : {} - {}".format(
    list(net.hosts())[0], list(net.hosts())[-1])
)