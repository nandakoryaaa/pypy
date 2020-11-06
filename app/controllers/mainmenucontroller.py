import pygame
from app.controllers.menucontroller import MenuController
from app.models.menuitem import MenuItem

class MainMenuController(MenuController):

  def process_item(self, game, item):
    if item.id == MenuItem.PLAY:
      game.score = 0
      game.lives = 3
      game.init_mode(game.MODE_PLAY)
      return True
    elif item.id == MenuItem.QUIT:
      game.init_mode(game.MODE_QUIT)
      return True

    return False