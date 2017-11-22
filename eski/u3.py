from socket import *
import time
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore





def fromU2():

	print 	"The server for U2 is ready to receive"
	while 1:
		messageFromU2, U2ClientAddress = fromU2serverSocket.recvfrom(2048)
		fromU2Lock.acquire()
		messageFromU2Reserve = messageFromU2
		print messageFromU2
		fromU2Flag=1
		fromU2Lock.release()


def toU2():

	print 	"The client for U2 is ready to receive"
	while 1:
		fromU2Lock.acquire()
		#if fromU2Flag==1:
		messageU2Reserve2=raw_input("Tell something")
		clientSocketToU2.sendto(messageU2Reserve2,(toU2ServerName, toU2ServerPort))
		print messageFromU2Reserve
		fromU2Flag=0
		fromU2Lock.release()
		




messageFromU2=""
messageFromU2Reserve=""

fromU2Flag=0
fromU2Lock=th.Lock()



toU2ServerName = "U2"
toU2ServerPort= 30022
clientSocketToU2 = socket(AF_INET, SOCK_DGRAM)


fromU2ServerPort=30003
fromU2serverSocket = socket(AF_INET, SOCK_DGRAM)
fromU2serverSocket.bind(("", fromU2ServerPort))


U2Acceptor =  th.Thread(target=fromU2)
U2Sender =  th.Thread(target=toU2)

