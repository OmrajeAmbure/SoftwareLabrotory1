import socket

while True:
    print("\n1. URL to IP")
    print("2. IP to URL")
    print("3. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        url = input("Enter URL: ")
        try:
            print("IP Address:", socket.gethostbyname(url))
        except:
            print("Invalid URL or not found.")

    elif ch == '2':
        ip = input("Enter IP Address: ")
        try:
            print("Host Name:", socket.gethostbyaddr(ip)[0])
        except:
            print("Invalid IP or not found.")

    elif ch == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")