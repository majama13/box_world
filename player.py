import pygame

class Player(pygame.sprite.Sprite):

	
	def __init__(self, window, player_size):
	
		super().__init__()
		self.window = window

		self.radius = player_size
		self.vel = 5

		self.image = pygame.Surface([2 * player_size, 2 * player_size], pygame.SRCALPHA)
		pygame.draw.circle(self.image, (0, 225, 0), self.image.get_rect().center, player_size, 3)  
		self.rect = self.image.get_rect(center = (self.window.get_width()//2, self.window.get_height()//2))


		
	def update(self, keys):
		pass



	def reset(self):
		#reset to original position
		self.rect.center = (self.window.get_width()//2, self.window.get_height()//2)
