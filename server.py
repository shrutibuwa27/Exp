import socket
def send_file(conn, filename):
with open(filename, 'rb') as file:
data = file.read(1024)
while data:
conn.send(data)
data = file.read(1024)
def main():
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)
print("Server is listening on port 12345...")
while True:
conn, addr = server_socket.accept()
print(f"Client connected from {addr}")
filename = conn.recv(1024).decode()
print(f"Receiving file: {filename}")
send_file(conn, filename)
print(f"File {filename} sent successfully!")
conn.close()
if __name__ == '__main__':
main()
