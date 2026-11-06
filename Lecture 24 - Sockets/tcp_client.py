import socket

HOST = '127.0.0.1'
PORT = 8080

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#     client.settimeout(10)
#     client.connect((HOST, PORT))
#     client.sendall("Hello from client".encode('utf-8'))
#     reply = client.recv(1024)
#     print(f"Response: {reply.decode('utf-8')}")



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.settimeout(10)
    client.connect((HOST, PORT))
    print("Type 'exit' to quit")

    while True:
        message = input("Enter message: ")
        
        if message.lower() == "exit":
            break

        client.sendall(message.encode('utf-8'))

        try:
            reply = client.recv(1024)
            print(f"Response: {reply.decode('utf-8')}")

            if reply.decode('utf-8') == 'exit':
                break

        except socket.timeout:
            print("Timeout")