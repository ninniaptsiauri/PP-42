import socket

HOST = '127.0.0.1'  # 127.0.0.1:8080
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print("Server is ready...")

    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received: {data.decode('utf-8')} from {addr}")
        
        server.sendto("Hello from server".encode('utf-8'), addr)