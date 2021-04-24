import socket
HOST_IP = "127.0.0.1"
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST_IP, serverPort))
serverSocket.listen()

print ("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print("Received words: ", sentence.decode())
    connectionSocket.send(sentence.upper())

connectionSocket.close()
serverSocekt.close()
