import socket

def start_server(host,port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        file_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file_data += data

        filename = "received_file.txt"
        with open(filename, "wb") as file:
            file.write(file_data)

        print(f"File '{filename}' received successfully")

        client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    start_server(host, port)