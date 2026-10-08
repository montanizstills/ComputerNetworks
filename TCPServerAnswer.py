### $Python3 TCPServerAnswer.py###

from socket import *
serverPort = 11000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while 1:
	connectionSocket, addr = serverSocket.accept()
	print ('Waiting for a message')
	sentence = connectionSocket.recv(1024)
	print ('Message from client: ' + sentence.decode('utf-8'))
	print (addr)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
