import socket
from threading import Thread
#from SocketServer import ThreadingMixIn

class ClientThread(Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)

		self.ip=ip
		self.port=port
		print ('[+] New server socket thread started for '+ip+ ':'+str(port))

	def run(self):
		while 1:
			data=conn.recv(1024)
			print ('Server received data:', data)
			message=input('Multithreaded Python server : Enter Response from Server/Enter exit:')
			message=message.encode()
			if message=='exit':
				break
			conn.send(message)

TCP_IP='0.0.0.0'
TCP_PORT=2004

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((TCP_IP,TCP_PORT))
threads=[]

while 1:
	s.listen(4)
	print('Multithreaded Python server: Waiting for connections from TCP listens...')
	(conn,(ip,port))=s.accept()
	t=ClientThread('0.0.0.0',2004)
	t.start()
	threads.append(t)

for i in threads:
	i.join()
