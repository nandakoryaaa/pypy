import pygame
from app.controllers.menucontroller import MenuController
from app.models.menuitem import MenuItem

class SetupController(MenuController):

  def __init__(self, view, model):
    super().__init__(view, model)
    self.display_mode_num = 0
    self.fullscreen = False

  def process_key(self, game, key_event):
    if key_event.key == pygame.K_ESCAPE:
      game.init_mode(game.MODE_MAIN_MENU)
      return True

    return False

  def process_item(self, game, item):
    if item.id == MenuItem.CANCEL:
      game.init_mode(game.MODE_MAIN_MENU)
      return True
    elif item.id == MenuItem.SAVE:
      config = game.config
      g = game.graphics
      if self.display_mode_num != g.display_mode_num or self.fullscreen != g.fullscreen:
        modes = g.get_display_modes()
        (width, height) = modes[self.display_mode_num]
        g.set_display_mode(width, height, self.fullscreen)
        config.window.width = width
        config.window.height = height
        config.window.fullscreen = self.fullscreen
      config.game.sfx_volume = game.audio.sfx_volume
      config.game.music_volume = game.audio.music_volume
      config.save()
      game.init_mode(game.MODE_MAIN_MENU)

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
    elif item.id == MenuItem.SCREEN_SIZE:
      self.display_mode_num = item.calc_position(step)
    elif item.id == MenuItem.FULLSCREEN:
      position = item.calc_position(step)
      self.fullscreen = True if position == 0 else False
    return False

