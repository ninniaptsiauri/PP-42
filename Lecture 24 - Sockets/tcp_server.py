import socket

HOST = '127.0.0.1'  # 127.0.0.1:8080
PORT = 8080

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server.bind((HOST, PORT))
    
#     server.listen(5)

#     print(f"Server is listening on port {HOST}:{PORT}")

#     conn, addr = server.accept()

#     with conn:
#         print("Connected", addr)

#         while True:
#             data = conn.recv(1024)

#             if not data: # b''
#                 break

#             print(f"Received: {data.decode('utf-8')}")

#             conn.sendall("Hello from server".encode('utf-8'))



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server is listening on port {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print("Connected", addr)
        print("Type 'exit' to quit")

        while True:
            data = conn.recv(1024)
            if not data: 
                break
            
            if data.decode('utf-8') == "exit":
                print("Client disconneted")
                break

            print(f'Received: {data.decode("utf-8")}')

            server_reply = input("Server reply: ")
            conn.sendall(server_reply.encode('utf-8'))

            if server_reply.lower() == "exit":
                print("Server disconneted")
                break

        
        