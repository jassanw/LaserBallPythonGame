import random
import os
import time
import pygame

black = [0,0,0]
pygame.init()
WIDTH, HEIGHT = 750,750

WIN = pygame.display.set_mode((WIDTH,HEIGHT))



def main():
	run = True
	FPS = 60
	yspeed = 0 #random.choice([-1,1]) * 4
	xspeed = 0 #random.choice([-1,1]) * 4
	xposition = random.randrange(0,WIDTH)
	yposition = random.randrange(0,HEIGHT)
	clock = pygame.time.Clock()

	def redraw_window():
		WIN.fill(black)
		pygame.draw.rect(WIN,(0,0,0),(0,0,20,20))
		pygame.draw.circle(WIN,(255,0,0),(0,0),20)
		pygame.display.update()

	while run:
		clock.tick(FPS)
		redraw_window()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		if(xposition + xspeed  >= WIDTH):
			xposition = WIDTH
			xspeed*=-1
		if (xposition + xspeed <= 0):
			xposition = 0
			xspeed*=-1
		if(xposition + xspeed  < WIDTH and xposition + xspeed > 0):
			xposition += xspeed
		
		if(yposition + yspeed>= HEIGHT):
			yposition = HEIGHT
			yspeed *= -1
		if(yposition + yspeed <= 0 ):
			yposition = 0
			yspeed *= -1
		if(yposition + yspeed  < HEIGHT and yposition + yspeed > 0):
			yposition += yspeed
	
		

	pygame.quit()

	
    


main()
