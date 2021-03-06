import pygame
from app.controllers.menucontroller import MenuController

class GameOverController(MenuController):

  def process_key(self, game, key_event):
    if key_event.key == pygame.K_ESCAPE:
      game.reset_mode(game.MODE_MAIN_MENU)
      return True
    return False

  def process_item(self, game, item):
    min_score = game.user_table.table[9].score
    if game.max_score > min_score:
      game.reset_mode(game.MODE_ENTER_NAME)
    else:
      game.reset_mode(game.MODE_MAIN_MENU)
    return True
