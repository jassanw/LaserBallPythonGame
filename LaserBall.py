import random
import os
import time
import pygame


pygame.init()

WIDTH,HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Laser Ball")



#LOAD IMAGES
PLAYER_SPRITE = pygame.image.load(os.path.join("PlayerSprite.png"))
BIG_BALL = pygame.image.load(os.path.join("assets","BIG_BALL.png"))
MEDIUM_BALL = pygame.image.load(os.path.join("assets","MEDIUM_BALL.png"))
SMALL_BALL = pygame.image.load(os.path.join("assets","SMALL_BALL.png"))

#BALL WIDTH INFO
BIG_BALL_DIM = 64
MED_BALL_DIM = 32
SMALL_BALL_DIM = 16


#BALL INFO
BIG_BALL_MAX_HEALTH = 8
MEDIUM_BALL_MAX_HEALTH = 5
SMALL_BALL_MAX_HEALTH = 2


class Player:
	def __init__(self, x,y,lives=3):
		self.x = x
		self.y = y
		self.lives = lives
		self.player_img = None
		self.laser_img = None
		self.max_lives = lives
		self.mask = pygame.mask.from_surface(self.player_img)
		self.lasers = []
		self.cool_down_counter = 0

class Ball:
	def __init__(self,x,y,x_vel,y_vel,health):
		self.x = x
		self.y = y
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.health = health
		self.ball_img = None
		self.OnDeath = None

	def draw(self,window):
		window.blit(self.ball_img,(self.x,self.y))

	def get_width(self):
		return self.ball_img.get_width()

	def get_height(self):
		return self.ball_img.get_height()

	def get_x_vel(self):
		return self.x_vel

	def set_x_vel(self,x_vel):
		self.x_vel = x_vel

	def get_y_vel(self):
		return self.y_vel

	def set_y_vel(self,y_vel):
		self.y_vel = y_vel

	def OnHit(self,collider):
		nv = pygame.math.Vector2(collider.x,collider.y) - pygame.math.Vector2(self.x,self.y)
		mv = pygame.math.Vector2(self.x_vel,self.y_vel).reflect(nv)
		self.x_vel = mv.x
		self.y_vel = mv.y
		self.move()

	def move(self):
		if self.y+self.y_vel+self.get_height()<HEIGHT and self.y+self.y_vel > 0:
			self.y+=self.y_vel
		elif self.y + self.y_vel + self.get_height() >= HEIGHT or self.y+self.y_vel<=0:
			self.y_vel*=-1

		if self.x+self.x_vel+self.get_width() < WIDTH and self.x+self.x_vel > 0:
			self.x += self.x_vel
		elif self.x+self.x_vel + self.get_width() >= WIDTH or self.x+self.x_vel <= 0:
			self.x_vel*=-1

	
		







class BigBall(Ball):
	def __init__(self,x,y,x_vel,y_vel):
		super().__init__(x,y,x_vel,y_vel,BIG_BALL_MAX_HEALTH)
		self.ball_img = BIG_BALL
		self.mask = pygame.mask.from_surface(self.ball_img)



	

class SmallBall(Ball):
	def __init__(self,x,y,x_vel,y_vel):
		super().__init__(x,y,x_vel,y_vel,SMALL_BALL_MAX_HEALTH)
		self.ball_img = SMALL_BALL
		self.mask = pygame.mask.from_surface(self.ball_img)
		

class MediumBall(Ball):
	def __init__(self,x,y,x_vel,y_vel):
		super().__init__(x,y,x_vel,y_vel,MEDIUM_BALL_MAX_HEALTH)
		self.ball_img = MEDIUM_BALL
		self.mask = pygame.mask.from_surface(self.ball_img)
		

def collide(obj1, obj2):
	offset_x = int(obj2.x - obj1.x)
	offset_y = int(obj2.y - obj1.y)
	return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None


def main():
	run = True
	FPS = 60
	clock = pygame.time.Clock()
	BigBall1 = BigBall(400,400,-5,5)
	BigBall2 = BigBall(100,200,5,5)
	MediumBall1 = MediumBall(600,600,-5,-5)
	MediumBall2 = MediumBall(500,300,-5,5)
	SmallBall2 = SmallBall(400,400,-5,5)
	SmallBall1 = SmallBall(60,60,5,-5)
	balls = []
	balls.append(BigBall1)
	balls.append(MediumBall1)
	balls.append(SmallBall1)
	balls.append(BigBall2)
	#balls.append(MediumBall2)
	#balls.append(SmallBall2)
	def redraw_window():
		WIN.fill([0,0,0])
		for ball in balls:
			ball.draw(WIN)
	
		#pygame.draw.rect(WIN,(255,0,0),(0,0,50,50))
		pygame.display.update()


	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		for ball in balls:
			ball.move()

		if collide(balls[0],balls[1]):
			balls[0].OnHit(balls[1])
			balls[1].OnHit(balls[0])

		if collide(balls[0],balls[2]):
			balls[0].OnHit(balls[2])
			balls[2].OnHit(balls[0])

		if collide(balls[0],balls[3]):
			balls[0].OnHit(balls[3])
			balls[3].OnHit(balls[0])

		if collide(balls[1],balls[2]):
			balls[1].OnHit(balls[2])
			balls[2].OnHit(balls[1])

		if collide(balls[1],balls[3]):
			balls[1].OnHit(balls[3])
			balls[3].OnHit(balls[1])

		if collide(balls[2],balls[3]):
			balls[2].OnHit(balls[3])
			balls[3].OnHit(balls[2])




		
					








	pygame.quit()

main()
