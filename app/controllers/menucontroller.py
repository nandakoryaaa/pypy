import pygame
from app.controllers.controller import Controller
from app.models.menuitem import MenuItem

class MenuController(Controller):

  def update(self, game, events):
    for event in events:
      key = event.key
      item = self.model.get_selected_item()
      exit = False
      if key == pygame.K_UP:
        self.model.prev_item()
        game.audio.play_sfx('apple')
      elif key == pygame.K_DOWN:
        self.model.next_item()
        game.audio.play_sfx('apple')
      elif key == pygame.K_LEFT:
        exit = self.process_control(game, item, -1)
      elif key == pygame.K_RIGHT:
        exit = self.process_control(game, item, 1)
      elif key == pygame.K_RETURN:
        exit = self.process_item(game, item)
      else:
        exit = self.process_key(game, event)
      if exit:
        return

    self.view.render()


  def process_item(self, game, item):
    pass

  def process_control(self, game, item, step):
    pass

  def process_key(self, game, key):
    pass