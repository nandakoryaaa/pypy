import pygame
from app.controllers.menucontroller import MenuController

class EnterNameController(MenuController):

  def __init__(self, view, model):
    super().__init__(view, model)
    self.font_map = view.graphics.get_font_params('white').map

  def process_key(self, game, key_event):
    if key_event.key == pygame.K_ESCAPE:
      game.reset_mode(game.MODE_MAIN_MENU)
      return True
    elif key_event.key == pygame.K_BACKSPACE:
      if len(self.view.user_name) > 0:
        self.view.user_name = self.view.user_name[:-1]
        self.view.ticks = 0
    else:
      char = key_event.unicode.upper()
      if (char == ' ' or char in self.font_map) and len(self.view.user_name) < 15:
        self.view.user_name += char
        self.view.ticks = 0
    return False

  def process_item(self, game, item):
    if len(self.view.user_name) == 0:
      self.view.user_name = 'NO NAME'
    game.user_name = self.view.user_name
    user_data = game.user_table.table[9]
    user_data.name = game.user_name
    user_data.score = game.max_score
    user_data.level = 1
    user_data.apples = game.apples
    user_data.length = game.max_length
    user_data.flags = 0
    game.user_table.sort()
    game.user_table.write()
    game.reset_mode(game.MODE_HALL_OF_FAME)
    return True
