    # Import socket module
import socket			

# Create a socket object
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)		

# Define the port on which you want to connect
port = 5000			

# connect to the server on local computer
s.connect(('192.168.0.100', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()	
	
