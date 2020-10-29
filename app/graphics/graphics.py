import pygame
import os

class Graphics:
	font_map = {
		'0': (0, 25),
		'1': (25, 15),
		'2': (40, 22),
		'3': (62, 22),
		'4': (84, 25),
		'5': (109, 23),
		'6': (132, 24),
		'7': (156, 19),
		'8': (175, 23),
		'9': (198, 23)
	}
	def __init__(self, w, h):
		os.environ['SDL_VIDEO_CENTERED'] = '0'
		pygame.init()
		self.screen_width = w
		self.screen_height = h
		self.context = pygame.display.set_mode((w, h)) #, pygame.FULLSCREEN)
		self.rect = pygame.Rect(0, 0, 0, 0)
		self.img_font = self.load_image('data/graphics/font.png')
		self.font_height = self.img_font.get_height()

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

	def draw_text(self, s, x, y):
		for char in s:
			char_data = self.font_map[char]
			char_width = char_data[1]
			rect = pygame.Rect(char_data[0], 0, char_width, self.font_height)
			self.context.blit(self.img_font, (x, y), rect)
			x += char_width + 2
