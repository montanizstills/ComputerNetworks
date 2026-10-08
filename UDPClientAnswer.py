###Python3###

from socket import *

# Blank start
# serverName = '132.238.114.25'
serverName = 'localhost'
# Blank end
# Blank start
serverPort = 12000
# Blank end
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    message = input('Input lowercase sentence:')
    # Blank start
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    # Blank end
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8'))

clientSocket.close()
