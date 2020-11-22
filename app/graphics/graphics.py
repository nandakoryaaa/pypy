import pygame
import os

class Graphics:
  def __init__(self):
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    self.width = 0
    self.height = 0
    self.context = None
    self.rect = pygame.Rect(0, 0, 0, 0)
    self.img_font = None
    self.font_list = {}
    self.font_params = None
    self.display_modes = self.get_display_modes()
    self.display_mode_num = 0
    self.fullscreen = 0
    pygame.init()

  def get_display_modes(self):
    return ((800,600), (1024,768), (1280,720), (1366,768), (1920,1080))

  def set_display_mode(self, width, height, fullscreen):
    check_mode = (width, height)
    found_mode = None
    mode_num = 0
    for mode in self.display_modes:
      if mode == check_mode:
        found_mode = mode
        break
      mode_num += 1
    if found_mode is None:
      mode_num = 0
      found_mode = self.display_modes[0]
    self.width = found_mode[0]
    self.height = found_mode[1]
    self.display_mode_num = mode_num
    self.fullscreen = fullscreen
    if fullscreen:
      self.context = pygame.display.set_mode(found_mode, pygame.FULLSCREEN)
    else:
      self.context = pygame.display.set_mode(found_mode)

  def load_font_img(self, img):
    self.img_font = self.load_image(img)

  def add_font_params(self, id, font_params):
    self.font_list[id] = font_params

  def set_font(self, id):
    if id in self.font_list:
      self.font_params = self.font_list[id]
    else:
      raise ValueError('font ' + id + ' not found')

  def get_font_params(self, id):
    if id in self.font_list:
      return self.font_list[id]
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
