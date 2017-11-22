from socket import *
import time
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore

def fromGateway():
	
	print 	"The server for Gateway is ready to receive"
	while 1:
		messageFromGateway, gatewayClientAddress = fromGatewayserverSocket.recvfrom(2048)
		fromGatewayLock.acquire()
		messageFromGatewayReserve = messageFromGateway
		print messageFromGateway
		fromGatewayFlag=1
		fromGatewayLock.release()

		#serverSocket.sendto(modifiedMessage, clientAddress)
		#if (messageFromGateway[-2:]=="U3")

def toGateway():

	print 	"The client for Gateway is ready to receive"
	while 1:
		fromU3Lock.acquire()
		if fromU3Flag==1:
			clientSocketToGateway.sendto(messageFromU3Reserve,(toGatewayServerName, toGatewayServerPort))
			print messageFromGatewayReserve
			fromU3Flag=0
		fromU3Lock.release()
		

def fromU3():

	print 	"The server for U3 is ready to receive"
	while 1:
		messageFromU3, U3ClientAddress = fromU3serverSocket.recvfrom(2048)
		fromU3Lock.acquire()
		messageFromU3Reserve = messageFromU3
		print messageFromU3
		fromU3Flag=1
		fromU3Lock.release()


def toU3():

	print 	"The client for U3 is ready to receive"
	'''while 1:
		fromGatewayLock.acquire()
		if fromGatewayFlag==1:
			clientSocketToU3.sendto(messageFromGatewayReserve,(toU3ServerName, toU3ServerPort))
			print messageFromGatewayReserve
			fromGatewayFlag=0
		fromGatewayLock.release()'''
	while 1:
		fromU3Lock.acquire()
		if fromU3Flag==1:
			messageFromU3Reserve=messageFromU3Reserve + "python krali"
			clientSocketToU3.sendto(messageFromU3Reserve,(toU3ServerName, toU3ServerPort))
			print messageFromU3Reserve
			fromU3Flag=0
		fromU3Lock.release()





messageFromGateway=""
messageFromU3=""
fromGatewayFlag=0
fromU3Flag=0

messageFromGatewayReserve=""
messageFromU3Reserve=""

fromGatewayLock=th.Lock()
fromU3Lock=th.Lock()

toGatewayServerName = "Gateway"
toGatewayServerPort= 10004
clientSocketToGateway = socket(AF_INET, SOCK_DGRAM)

toU3ServerName = "U3"
toU3ServerPort= 30003
clientSocketToU3 = socket(AF_INET, SOCK_DGRAM)

fromGatewayServerPort=30002
fromGatewayserverSocket = socket(AF_INET, SOCK_DGRAM)
fromGatewayserverSocket.bind(("",fromGatewayServerPort))

fromU3ServerPort=30022
fromU3serverSocket = socket(AF_INET, SOCK_DGRAM)
fromU3serverSocket.bind(("", fromU3ServerPort))

gatewayAcceptor =  th.Thread(target=fromGateway)
gatewaySender =  th.Thread(target=toGateway)
U3Acceptor =  th.Thread(target=fromU3)
U3Sender =  th.Thread(target=toU3)




