import socket
import pickle

class Network(object):
	"""docstring for Network"""
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = "192.168.1.5"
		self.port = 5555
		self.addr = (self.server, self.port)
		self.p = self.connect()
		#print(self.id)

	def getP(self):
		return self.p

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))
		except Exception as e:
			print(e)

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)




# net = Network()

# print(net.send("ushijima"))
# print(net.send("akaashi"))
# print(net.send("bokuto"))
# print(net.send("oikawa"))
