from socket import *
import time
serverName = "Gateway"
serverPort = 2002
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence:")
message += "u1_t3"
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
