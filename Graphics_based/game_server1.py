#!/usr/bin/python3

#game server

import socket      
from _thread import *
import time   
import sys          

port = 12321

map={}

gameid=4

def create_game(list_of_game_instances):
	global map
	global gameid
	print("hello11")
	# conn.send(bytes(str(gameid), 'utf8'))
	# conn.recv(10)
	list_of_game_instances.append(gameid)
	map[gameid]={}
	print("game created")
	gameid+=1

def thread_player_handle(conn,iid):
	global map
	while (True):
		    # time.sleep(1)
		    print('hii')
		    l=len(list_of_game_instances)
		    conn.send(bytes(str(l), 'utf8'))
		    conn.recv(1024)
		    for i in list_of_game_instances:
		    	 conn.send(bytes(str(i), 'utf8'))
		    	 conn.recv(1024)

		    gameid=conn.recv(10).decode('utf-8')
		    conn.send(b' ')

		    print(gameid)
		    if(gameid=='999'):
		    	create_game(list_of_game_instances)
		    	continue

		    gameid=int(gameid)
		    d=conn.recv(10).decode('utf-8')
		    conn.send(b' ')
		    print("Game id : ",gameid)
		    d=int(d)
		    print(d)
		    if(d==1):
		    	print("Get Request ")
		    	g=conn.recv(10).decode('utf-8')
		    	#conn.send(b' ')
		    	g=int(g)
		    	conn.send(bytes(str(len(map[g])), 'utf8'))
		    	conn.recv(10)
		    	for k,v in map[g].items():
		    		conn.send(bytes(str(k), 'utf8'))
		    		conn.recv(10)
		    		conn.send(bytes(str(v), 'utf8'))
		    		conn.recv(10)
		    elif (d==3):
		    	print("Join Game : ")
		    	g=conn.recv(10).decode('utf-8')
		    	#conn.send(b' ')
		    	g=int(g)
		    	if iid not in map[g]:
		    		map[g][iid]=0
		    		conn.send(bytes(str(0), 'utf8'))
		    		conn.recv(10)
		    	else:
		    		print("Already Joined the game")
		    		conn.send(bytes(str(1), 'utf8'))
		    		conn.recv(10)

		    elif (d==2):
		    	print("Game Move : ")
		    	g=conn.recv(10).decode('utf-8')
		    	conn.send(b' ')
		    	d=conn.recv(10).decode('utf-8')
		    	#conn.send(b' ')
		    	g=int(g)
		    	d=int(d)
		    	print(g,d)
		    	if iid not in map[g]:
		    		print("First Join the game")
		    		conn.send(bytes(str(0), 'utf8'))
		    		conn.recv(10)
		    	else:
		    		map[g][iid]+=d
		    		print(iid," : Score ->",map[g][iid])
		    		conn.send(bytes(str(1), 'utf8'))
		    		conn.recv(10)

		    print("Done!")


if __name__ == "__main__":
	s = socket.socket()            
	# host = socket.gethostbyname()
	print("Enter Server port : ")
	port=int(input())
	try:     
		s.bind(('', port)) 
	except OSError:
		print("Port already in use")
		sys.exit(0)

	try:         
		s.listen(5)                     

		print ('Server listening....')
		list_of_game_instances=[0,1,2,3]
		for i in list_of_game_instances:
			map[i]={}
		iid=0

		while (True):
		    conn, addr = s.accept()    
		    print('Got connection from', addr)
		    conn.send(b'Thank you for connecting')
		    conn.recv(1024)
		    iid+=1
		    conn.send(bytes(str(iid), 'utf8'))
		    conn.recv(10)
		    print("New Thread Created : ",iid)
		    start_new_thread(thread_player_handle,(conn,iid))
		    # data = conn.recv(1024).decode('utf-8')
		    #print('Server received', repr(data))

	except Exception as msg:
		print(msg)
	finally:
		s.close()
		print("Port Closed")