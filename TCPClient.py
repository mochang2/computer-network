import socket

HOST_IP = "127.0.0.1"
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST_IP, serverPort))
sentence = input("Input sentence: ")
clientSocket.sendall(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print ("From Server:", modifiedSentence.decode("ascii"))

clientSocket.close()
