import socket

def send_file(server_host, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    with open(file_path, "rb") as file:
        file_data = file.read()

    # Display the contents of the file
    print(f"Contents of '{file_path}':")
    print(file_data.decode("utf-8"))

    # Send the file data
    client_socket.sendall(file_data)

    print(f"File '{file_path}' sent successfully")

    client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 12345
    file_to_send = "file_to_send.txt"  #Include file in same directory as client script
    send_file(server_host, server_port, file_to_send)