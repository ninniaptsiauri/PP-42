import socket

HOST = '127.0.0.1'  # 127.0.0.1:8080
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(5)
    client.sendto("Hello from client".encode('utf-8'), (HOST, PORT))

    try: 
        data, _ = client.recvfrom(1024)
        print(f"Response: {data.decode('utf-8')}")

    except socket.timeout:
        print("Timeout")