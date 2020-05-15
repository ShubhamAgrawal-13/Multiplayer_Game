import pygame
from network import Network
from player import Player

width = 500
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

# clientNumber = 0

# def read_pos(st):
# 	st=st.split(",")
# 	return int(st[0]),int(st[1])

# def make_pos(tup):
# 	return str(tup[0])+","+str(tup[1])


def reDrawWindow(win, player,player2):
	win.fill((255,255,255))
	player.draw(win)
	player2.draw(win)
	pygame.display.update()


def main():
	run = True
	n= Network()
	p = n.getP()
	clock = pygame.time.Clock()
	while(run):
		clock.tick(60)
		p2 = n.send(p)
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				run = False
				pygame.quit()


		p.move()
		reDrawWindow(win,p,p2)	

if __name__ == '__main__':
	main()