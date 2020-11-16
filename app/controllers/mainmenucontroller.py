import pygame
from app.controllers.menucontroller import MenuController
from app.models.menuitem import MenuItem

class MainMenuController(MenuController):

  def process_item(self, game, item):
    if item.id == MenuItem.PLAY:
      game.score = 0
      game.max_score = 0
      game.length = 0
      game.max_length = 0
      game.apples = 0
      game.lives = 3
      game.init_mode(game.MODE_START_LEVEL)
      return True
    elif item.id == MenuItem.QUIT:
      game.init_mode(game.MODE_QUIT)
      return True
    elif item.id == MenuItem.QUIT:
      game.init_mode(game.MODE_QUIT)
      return True
    elif item.id == MenuItem.HALL_OF_FAME:
      game.init_mode(game.MODE_HALL_OF_FAME)
      return True

    return False