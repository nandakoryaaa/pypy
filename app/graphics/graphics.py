import pygame

class Graphics:
	def __init__(self, w, h):
		pygame.init()
		self.screen_width = w
		self.screen_height = h
		self.context = pygame.display.set_mode((w, h))
		self.rect = pygame.Rect(0, 0, 0, 0)

	def draw_rect(self, x, y, w, h, color):
		rect = self.rect
		rect.left = x
		rect.top = y
		rect.width = w
		rect.height = h
		self.context.fill(color, rect)

	def update(self):
		pygame.display.update()