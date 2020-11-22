import pygame
from app.controllers.menucontroller import MenuController
from app.models.menuitem import MenuItem

class PauseController(MenuController):

  def process_key(self, game, key_event):
    if key_event.key == pygame.K_ESCAPE:
      game.pop_mode()
      return True

    return False

  def process_item(self, game, item):
    if item.id == MenuItem.MAIN_MENU:
      game.reset_mode(game.MODE_MAIN_MENU)
      return True
    elif item.id == MenuItem.CONTINUE:
      game.pop_mode()
      return True

    return False

  def process_control(self, game, item, step):
    if item.id == MenuItem.SOUND:
      volume = item.calc_value(0.1 * step)
      game.audio.set_sfx_volume(volume)
      game.audio.play_sfx('apple')
    elif item.id == MenuItem.MUSIC:
      volume = item.calc_value(0.1 * step)
      game.audio.set_music_volume(volume)

    return False

