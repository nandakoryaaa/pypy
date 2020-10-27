import pygame
import os

class Graphics:
	def __init__(self, w, h):
		os.environ['SDL_VIDEO_CENTERED'] = '0'
		pygame.init()
		self.screen_width = w
		self.screen_height = h
		self.context = pygame.display.set_mode((w, h)) #, pygame.FULLSCREEN)
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

	def load_image(self, file):
		img = pygame.image.load(file).convert_alpha()
		return img

	def draw_image(self, image, x, y):
		self.context.blit(image, (x,y))

	def fill(self, color):
		self.context.fill(color)