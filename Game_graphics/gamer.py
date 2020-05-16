import pygame
from network import Network
from player import Player
from sys import argv

width = 350
height = 350

win = pygame.display.set_mode((width,height))

def reDrawWindow(win, players):
	win.fill((255,255,255))
	for i in players:
		i.draw(win)
	pygame.display.update()



def main():
	run = True
	port=5555

	n= Network(port)
	p = n.getPlayer()

	clock = pygame.time.Clock()

	while(run):
		clock.tick(60)
		players = n.send(p)

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				run = False
				pygame.quit()


		p.move()
		reDrawWindow(win,players)	



if __name__ == '__main__':
	pygame.display.set_caption(str(argv[1]))
	main()