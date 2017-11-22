from socket import *
import time
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore


print "Hello from U2"

def fromU3(flagg):

	print 	"The server for U3 is ready to receive"
	while 1:
		messageFromU3, U3ClientAddress = fromU3serverSocket.recvfrom(2048)
		fromU3Lock.acquire()
		messageFromU3Reserve = messageFromU3
		print messageFromU3
		flagg=1
		fromU3Lock.release()


def toU3(flagg):

	print 	"The client for U3 is ready to receive"
	#fromU3Flag=0

	'''while 1:
		fromGatewayLock.acquire()
		if fromGatewayFlag==1:
			clientSocketToU3.sendto(messageFromGatewayReserve,(toU3ServerName, toU3ServerPort))
			print messageFromGatewayReserve
			fromGatewayFlag=0
		fromGatewayLock.release()'''
	while 1:
		fromU3Lock.acquire()
		if flagg==1:
			messageFromU3Reserve=messageFromU3Reserve + "python krali"
			clientSocketToU3.sendto(messageFromU3Reserve,(toU3ServerName, toU3ServerPort))
			print messageFromU3Reserve
			flagg=0
		fromU3Lock.release()




print "Hello from U2 2"

messageFromU3=""
fromU3Flag=0

messageFromU3Reserve=""

fromU3Lock=th.Lock()

print "Hello from U2 3"

toU3ServerName = "node-1"
toU3ServerPort= 30603
clientSocketToU3 = socket(AF_INET, SOCK_DGRAM)


fromU3ServerPort=30622
fromU3serverSocket = socket(AF_INET, SOCK_DGRAM)
fromU3serverSocket.bind(("", fromU3ServerPort))

print "Hello from U2 4 "

U3Acceptor =  th.Thread(target=fromU3, args="fromU3Flag")
U3Sender =  th.Thread(target=toU3, args="fromU3Flag")

U3Acceptor.start()
U3Sender.start()
U3Acceptor.join()
U3Sender.join()

print "Hello from U2 5"

fromU3serverSocket.close()