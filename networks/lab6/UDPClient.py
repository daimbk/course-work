from socket import *

serverName = '172.30.69.158'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print("Received message from %s port %s"%(serverAddress[0],serverAddress[1]))

print(modifiedMessage.decode())
clientSocket.close()
