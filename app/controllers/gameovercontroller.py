import pygame
from app.controllers.menucontroller import MenuController

class GameOverController(MenuController):

  def process_key(self, game, key):
    if key == pygame.K_ESCAPE:
      game.reset_mode(game.MODE_MAIN_MENU)
      return True

    return False

  def process_item(self, game, item):
      game.reset_mode(game.MODE_MAIN_MENU)
      return True
