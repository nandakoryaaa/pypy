import pygame
import os

class Graphics:
  def __init__(self, width, height):
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    pygame.init()
    self.width = width
    self.height = height
    self.context = pygame.display.set_mode((width, height)) #, pygame.FULLSCREEN)
    self.rect = pygame.Rect(0, 0, 0, 0)
    self.img_font = None
    self.font_list = {}
    self.font_params = None

  def load_font_img(self, img):
    self.img_font = self.load_image(img)

  def add_font_params(self, id, font_params):
    self.font_list[id] = font_params

  def set_font(self, id):
    if id in self.font_list:
      self.font_params = self.font_list[id]
    else:
      raise ValueError('font ' + id + ' not found')

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
    fp = self.font_params
    cl = fp.chars_in_line
    rect = self.rect
    rect.width = fp.char_width
    rect.height = fp.char_height
    for char in s:
      if char != ' ':
        pos = fp.map.find(char)
        rect.left = fp.start_x + (pos % cl) * fp.char_width
        rect.top = fp.start_y + (pos // cl) * fp.char_height
        self.context.blit(self.img_font, (x, y), rect)
      x += fp.char_width + fp.char_spacing
