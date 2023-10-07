import pygame

class Wall(pygame.Rect):

	
	def __init__(self, window, player_size):
	
		#super().__init__()
		self.window = window
		self.WHITE = (225,225,225)
		self.rect = pygame.Rect(self.window.get_width()//2, 0, 0, 0)
		self.image = pygame.Surface([self.rect.width, self.rect.height])
		self.left_wall = -player_size
		self.right_wall = self.window.get_width() + player_size
		self.vel = 5


	def update(self, keys):

		self.image.fill(self.WHITE)
		
		if self.rect.center[0] < self.window.get_width():
			self.rect.x += keys[pygame.K_LEFT] * self.vel
			self.left_wall += keys[pygame.K_LEFT] * self.vel
			self.right_wall += keys[pygame.K_LEFT] * self.vel
		if self.rect.center[0] > 0:
			self.rect.x -= keys[pygame.K_RIGHT] * self.vel
			self.left_wall -= keys[pygame.K_RIGHT] * self.vel
			self.right_wall -= keys[pygame.K_RIGHT] * self.vel
		#print(self.left_wall, self.right_wall)


	def draw(self):
		pygame.draw.line(self.window, 
						self.WHITE, 
						(self.left_wall, 0), 
						(self.left_wall, self.window.get_height())
		)
		pygame.draw.line(self.window, 
						self.WHITE, 
						(self.right_wall, 0), 
						(self.right_wall, self.window.get_height())
		)
	

	def reset(self):
		pass

