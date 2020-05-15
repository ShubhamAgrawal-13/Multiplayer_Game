#!/usr/bin/python3

#player program (client)


import socket      
import time
from colorama import Fore


def send_move(s,gameid):
	s.send(bytes(str(gameid), 'utf8'))
	s.recv(10)
	print("Enter move : ")
	move=int(input())
	s.send(bytes(str(move), 'utf8'))
	#s.recv(10)
	ll=s.recv(10).decode('utf-8')
	s.send(b' ')
	if(ll=='1'):
		print("Updated the move")
	else:
		print("First Join the game")


def get_request(s,gameid,client_id):
	s.send(bytes(str(gameid), 'utf8'))
	#s.recv(10)
	ll=s.recv(10).decode('utf-8')
	s.send(b' ')
	ll=int(ll)
	print()
	print("Current Status of game with gameid : ",gameid)

	if(ll==0):
		print("Currently, No players in the game")
		return

	for i in range(ll):
		playerid=s.recv(10).decode('utf-8')
		s.send(b' ')
		move=s.recv(10).decode('utf-8')
		s.send(b' ')
		if(int(playerid)==client_id):
			print(Fore.GREEN+"Your Score : ",move)
		else:
			print(Fore.RED+"Player with id : ",playerid,"----> Score : ",move)
	print(Fore.WHITE+' ')

def join_game(s,gameid):
	s.send(bytes(str(gameid), 'utf8'))
	#s.recv(10)
	ll=s.recv(10).decode('utf-8')
	s.send(b' ')
	if(ll=='1'):
		print("Already Joined the game")
	else:
		print("Joined successfully")



if __name__ == "__main__": 
	s = socket.socket()          
	print("Enter Server port : ")
	port=int(input())
	s.connect(('127.0.0.1', port))
	print(s.recv(1024).decode('utf-8'))
	s.send(b' ')
	client_id=s.recv(1024).decode('utf-8')
	s.send(b' ')
	client_id=int(client_id)
	while(1):
		print('hii')
		# time.sleep(1)
		length=s.recv(1024).decode('utf-8')
		s.send(b' ')
		for i in range(int(length)):
			gameid=s.recv(1024).decode('utf-8')
			print("To join a Game with gameid : ",gameid)
			s.send(b' ')
		print("To create a new game : [type 999]")
		print("Enter gameid or [type 999]: ")
		inp=input()

		# if(inp=='999'):
		# 	s.send(bytes(str(1), 'utf8'))
		# 	s.recv(10)
		# else:
		# 	s.send(bytes(str(0), 'utf8'))
		# 	s.recv(10)
		
		if(inp=='999'):
			s.send(bytes(str(inp), 'utf8'))
			s.recv(10)
			print("successfully created game")
			continue
		else:
			gameid=int(inp)
			s.send(bytes(str(gameid), 'utf8'))
			s.recv(10)
			print("1 : for get request\n2 : for making a move\n3 : for joining a game")
			d=int(input())
			s.send(bytes(str(d), 'utf8'))
			s.recv(10)
			print("Good")
			if(d==1):
				get_request(s,gameid,client_id)
			elif(d==2):
				send_move(s,gameid)
			elif(d==3):
				join_game(s,gameid)
			else:
				print("Invalid Choice")
	s.close()