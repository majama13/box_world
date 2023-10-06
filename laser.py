import pygame

class Laser(pygame.sprite.Sprite):

	

	def __init__(self, radius):
	
		super().__init__()
		self.radius = radius
		self.vel = 5

		self.image = pygame.Surface([4, 24])
		self.image.fill((225, 0, 0))
		self.rect = self.image.get_rect()
		self.lasershot = False
		
		

	def update(self, keys, player_x, player_y):
	
		#update laser movement
		if not self.lasershot:
			if keys[pygame.K_SPACE]:
				self.lasershot = True
				self.rect.y = player_y - 2 * self.radius
				self.rect.x = player_x
		elif self.rect.y < 0:
			self.lasershot = False
		else:
			self.rect.y -= 2 * self.vel
