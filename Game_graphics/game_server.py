import socket
from _thread import *
import sys
import pickle
from player import Player

def pack(data):
	return pickle.dumps(data)

def unpack(data):
	return pickle.loads(data)


server=""
port=5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.bind((server,port))
	print("Server binded to port",port)
except socket.error as e:
	str(e)

s.listen(2)
print("Listening .....")


players = []

def handle_client(conn, player):
	conn.send(pack(players[player]))
	while(1):
		try:
			data = unpack(conn.recv(2048))
			players[player]=data 

			if not data:
				print("Disconnected")
				break

			conn.sendall(pack(players))

		except Exception as e:
			print(e)
			break
	
	print("Lost Connection")
	# players.pop(player)
	conn.close()


import random
import numpy as np
## Server loop
currentPlayer = 0
while(1):
	conn, addr = s.accept()
	print("Connected to ",addr)
	xi = random.randint(15,335) 
	yi = random.randint(15,335) 
	color = tuple(np.random.choice(range(256), size=3))
	players.append(Player(xi,yi,30,30,color))
	start_new_thread(handle_client,(conn,currentPlayer))
	currentPlayer+=1