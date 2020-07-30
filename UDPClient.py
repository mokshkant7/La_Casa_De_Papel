import socket
from Crypto.Cipher import AES

obj2 = AES.new(' Moksh is the Professor ', AES.MODE_CBC, 'This is an IV456')

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 21111)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print(msgFromServer)
print("decrypting...")
print(obj2.decrypt(msgFromServer[0]))


#msg = "Message from Server {}".format(obj2.decrypt(msgFromServer))
#print(msg)
