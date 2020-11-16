import pygame
from app.controllers.menucontroller import MenuController

class StartLevelController(MenuController):

  def process_key(self, game, key_event):
    if key_event.key == pygame.K_ESCAPE:
      game.init_mode(game.MODE_MAIN_MENU)
      return True
    return False

  def process_item(self, game, item):
    game.init_mode(game.MODE_PLAY)
    return True
