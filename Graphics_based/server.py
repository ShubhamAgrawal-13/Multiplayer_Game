import socket
from _thread import *
import sys
import pickle
from player import Player

server="192.168.1.5"
port=5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.bind((server,port))
	print("Server binded to port",port)
except socket.error as e:
	str(e)

s.listen(2)
print("Listening .....")

def read_pos(st):
	st=st.split(",")
	return int(st[0]),int(st[1])

def make_pos(tup):
	return str(tup[0])+","+str(tup[1])


players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]

def handle_client(conn, player):
	reply=""
	conn.send(pickle.dumps(players[player]))
	while(1):
		try:
			data = pickle.loads(conn.recv(2048))
			players[player]=data 

			if not data:
				print("Disconnected")
				break
			else:
				if(player == 1):
					reply=players[0]
				else:
					reply=players[1]
				print("Received : ",data)
				print("Sending : ",reply)

			conn.sendall(pickle.dumps(reply))

		except Exception as e:
			print(e)
			break
	
	print("Lost Connection")
	conn.close()

currentPlayer = 0

while(1):
	conn, addr = s.accept()
	print("Connected to ",addr)

	start_new_thread(handle_client,(conn,currentPlayer))
	currentPlayer+=1

