from socket import *
serverPort = 2001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print "The server is ready to receive"
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        if message[-2:-1] == "U3" :
        	print "test!!!"
        modifiedMessage = message.upper()
        print modifiedMessage
        serverSocket.sendto(modifiedMessage, clientAddress)
