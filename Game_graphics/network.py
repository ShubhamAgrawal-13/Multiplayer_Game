import socket
import pickle

def pack(data):
	return pickle.dumps(data)

def unpack(data):
	return pickle.loads(data)



class Network(object):
	"""docstring for Network"""
	def __init__(self,port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = ""
		self.port = port
		self.addr = (self.server, self.port)
		self.player = None
		try:
			## make connection
			self.client.connect(self.addr)
			## receive player object
			self.player = unpack(self.client.recv(2048))
		except:
			print("Some Error occurred")
			self.client.close()


	def getPlayer(self):
		return self.player
	

	def send(self, data):
		try:
			self.client.send(pack(data))
			return unpack(self.client.recv(2048))
		except socket.error as e:
			print(e)