### $python3 TCPClientAnswer.py ###
from socket import *
#serverName = '132.238.105.102'
serverName = 'localhost'
serverPort = 11000

while 1:
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	sentence = input('Input lowercase sentence:')
	clientSocket.send(sentence.encode('utf-8'))
	modifiedSentence = clientSocket.recv(1024)
	print ('From Server:', modifiedSentence.decode('utf-8'))
	clientSocket.close()


