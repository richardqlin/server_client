import socket

host='0.0.0.0'
port =2004

message=input('Client A: Enter message/ Enter exit:')
message=message.encode()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while message!='exit':
	s.send(message)
	data=s.recv(1024)
	print ('Client2 received data:',data)

	message=input('Client A: Enter message/ Enter exit:')
	message=message.encode()

s.close()