import pygame

class Wall(pygame.Rect):

	
	def __init__(self, window, player_size):
	
		#super().__init__()
		self.window = window
		self.rect = pygame.Rect(self.window.get_width()//2, 0, 0, 0)
		self.image = pygame.Surface([self.rect.width, self.rect.height])
		self.left_wall = -player_size
		self.right_wall = self.window.get_width() + player_size
		self.vel = 5

	def update(self, keys):

		self.image.fill((225,225,225))
		
		if self.rect.center[0] < self.window.get_width():
			self.rect.x += keys[pygame.K_LEFT] * self.vel
			self.left_wall += keys[pygame.K_LEFT] * self.vel
			self.right_wall += keys[pygame.K_LEFT] * self.vel
		if self.rect.center[0] > 0:
			self.rect.x -= keys[pygame.K_RIGHT] * self.vel
			self.left_wall -= keys[pygame.K_RIGHT] * self.vel
			self.right_wall -= keys[pygame.K_RIGHT] * self.vel
		#print(self.left_wall, self.right_wall)
	
	def reset(self):
		pass

def main():
	WIDTH, HEIGHT = 300, 600
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	game_area = pygame.Rect(0, 0, WIDTH, HEIGHT)
	right_wall = Wall(window)

	run = True
	while run:
		pygame.time.Clock().tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:					
				print(pygame.key.name(event.key))

		keys = pygame.key.get_pressed()
		
		#update
		right_wall.update(keys)
		
		#draw
		window.fill(0)

		window.blit(right_wall.image, (right_wall.rect.x, right_wall.rect.y))

		pygame.display.flip()

	pygame.quit()
	exit()

