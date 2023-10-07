import pygame
import math

class Laser(pygame.sprite.Sprite):

	

	def __init__(self, window, radius):
	
		super().__init__()
		self.window = window
		self.radius = radius
		self.vel = 5

		self.image = pygame.Surface([4, 24])
		self.image.fill((225, 0, 0))
		self.rect = self.image.get_rect()
		self.lasershot = False
		self.theta = 3 * math.pi/2
		self.clockwise = True
		self.coord = (self.window.get_width()//2,0)
		
		

	def update(self, laser_switch, laser_hold, obstacles):

		# Update ray angle
		self.update_theta(laser_switch, laser_hold) 

		# Record ray and segment
		ray = self._calculate_ray()
		segment_list = self._list_line_segments(obstacles)

		# Calculate intersections
		#self.coord_list = []
		t1 = 300

		for obst in segment_list:
			for seg in obst:
				if not(ray[1] == seg[1] or ray[3] == seg[3]): # Make sure not parallel
					t2 = (ray[1] * (seg[2] - ray[2]) + ray[3] * (ray[0] - seg[0]))/(seg[1] * ray[3] - seg[3] * ray[1])
					if 0 < t2 < 1:
						#t1x = (seg[0] + seg[1] * t2 - ray[0])/ray[1]
						t1y = (seg[2] + seg[3] * t2 - ray[2])/ray[3]
						#print('t1x ', t1x)
		#				print('t1y ', t1y)
						if t1y > 0:
							t1 = min(t1, t1y)

		#print('pos t1 ', t1)
		#print(t2)

		x = ray[0] + ray[1] * t1
		y = ray[2] + ray[3] * t1
		#self.coord_list.append((x,y))	
		self.coord = (x, y)
		#print('coord ', (x, y))	



	def update_theta(self, laser_switch, laser_hold):

		if laser_hold:
			pass
		elif self.clockwise:
			if laser_switch or self.theta > 2 * math.pi:
				self.clockwise = False
				self.theta -= math.radians(1)
			else: 
				self.theta += math.radians(1)
		else:
			if laser_switch or self.theta < math.pi: 
				self.clockwise = True
				self.theta += math.radians(1)
			else: 
				self.theta -= math.radians(1)
		
		#print('theta ', self.theta)


	def _list_line_segments(self, obstacles):
		
		# Represent lines in parametric form: Point + Direction * T
		# broken into x and y components (x,y) + (delta x, delta y) * t
		# so that a segment is represented by [x, delta x, y, delta y]
		segment_list = []

		for obst in obstacles:
			top = [obst.rect.x, obst.rect.width, obst.rect.y, 0]
			bottom = [obst.rect.x, obst.rect.width, obst.rect.y + obst.rect.height, 0]
			left = [obst.rect.x, 0, obst.rect.y, obst.rect.height]
			right = [obst.rect.x + obst.rect.width, 0, obst.rect.y, obst.rect.height]
			
			segment_list.append([top, bottom, left, right])
		#print('seg list ', segment_list)
		return segment_list



	def _calculate_ray(self):

		ray = [self.window.get_width()//2, math.cos(self.theta), self.window.get_height()//2, math.sin(self.theta)]
		#print('ray ', ray)
		return ray

	

	def draw(self):
		
		pygame.draw.line(self.window, 
					(225, 0, 0), 
					(self.window.get_width()//2, self.window.get_height()//2), 
					self.coord
		)




