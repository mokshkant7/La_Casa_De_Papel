import socket
from Crypto.Cipher import AES

obj = AES.new(' Moksh is the Professor ', AES.MODE_CBC, 'This is an IV456')

localIP     = "127.0.0.1"
localPort   = 21111
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
ciphertext = obj.encrypt(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams
# to decrypt readme just convert spanish to english

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(ciphertext, address)
