import socket
import os
soc = socket.socket()
host = "127.0.0.1"
port = 8084
soc.bind((host,port))
soc.listen(1)
print("Host Name:",host)
print("Waiting For Client To Connect")
conn, addr =soc.accept()
print(addr, "Client Has Connected To Server")
fileName = input(str("File Name:"))
file = open(fileName, 'rb')
fileData = file.read(1024)
conn.send(fileData)
print("File Sent")