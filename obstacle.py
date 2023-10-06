import pygame
import random

class Obstacle(pygame.sprite.Sprite):

	
	def __init__(self, window, player_size, parent = None):
	
		super().__init__()
		self.window = window
		self.image = pygame.Surface([0, 0])
		self.rect = pygame.Rect([0, 0, 0, 0])
		self.vel = 5
		self.min_size = player_size * 2
		self.color = (225, 225, 225)
		self.parent = parent
		
	
	def spawn(self, left_wall = -40, right_wall = 340, initial_y = 10):

		#get random values for x, y, width, height
		self.rect.x = random.randint(left_wall, right_wall)
		self.rect.width = random.randint(self.min_size, self.window.get_width()//2)
		if self.rect.x + self.rect.width > right_wall:
			self.rect.x = right_wall - self.rect.width
		self.rect.height = random.randint(self.min_size, self.window.get_height()//2)
		if self.parent and self.parent.rect.y < 0:
			self.rect.y = self.parent.rect.y - (self.rect.height + 2 * self.min_size)
		else:
			self.rect.y = initial_y - self.rect.height

		#update the surface to the above values
		self.image = pygame.Surface([self.rect.width, self.rect.height])
		self.image.fill(self.color)
		#self.rect = self.image.get_rect(x = self.rect.x, y = self.rect.y)

		
	def update(self, keys, wall_pos, left_wall, right_wall, restart = False):

		#update obstacle position
		if self.rect.y > self.window.get_height():
			self.spawn(left_wall, right_wall)

		if wall_pos < self.window.get_width():
			self.rect.x += keys[pygame.K_LEFT] * self.vel
		if wall_pos > 0:
			self.rect.x -= keys[pygame.K_RIGHT] * self.vel
		self.rect.y += keys[pygame.K_UP] * self.vel
		self.rect.y -= keys[pygame.K_DOWN] * self.vel
	
	
	def reset(self):
		self.spawn()


