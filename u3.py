from socket import *
import time
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore


print "Hello from U3"


def fromU2(flagg):

	print 	"The server for U2 is ready to receive"
	while 1:
		messageFromU2, U2ClientAddress = fromU2serverSocket.recvfrom(2048)
		fromU2Lock.acquire()
		messageFromU2Reserve = messageFromU2
		print messageFromU2
		flagg=1
		fromU2Lock.release()


def toU2(flagg):

	print 	"The client for U2 is ready to receive"
	while 1:
		fromU2Lock.acquire()
		#if fromU2Flag==1:
		messageU2Reserve2=raw_input("Tell something")
		clientSocketToU2.sendto(messageU2Reserve2,(toU2ServerName, toU2ServerPort))
		print messageFromU2Reserve
		flagg=0
		fromU2Lock.release()
		



print "Hello from U3 2"

messageFromU2=""
messageFromU2Reserve=""

fromU2Flag=0
fromU2Lock=th.Lock()


print "Hello from U3 3 "

toU2ServerName = "node-0"
toU2ServerPort= 30622
clientSocketToU2 = socket(AF_INET, SOCK_DGRAM)


fromU2ServerPort=30603
fromU2serverSocket = socket(AF_INET, SOCK_DGRAM)
fromU2serverSocket.bind(("", fromU2ServerPort))


print "Hello from U3 4"
U2Acceptor =  th.Thread(target=fromU2, args="fromU2Flag")
U2Sender =  th.Thread(target=toU2, args="fromU2Flag")

U2Acceptor.start()
U2Sender.start()

U2Acceptor.join()
U2Sender.join()
print "Hello from U3 5"

fromU2serverSocket.close()