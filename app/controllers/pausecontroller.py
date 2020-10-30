import pygame
from app.controllers.controller import Controller

class PauseController(Controller):
  MENU_SOUND = 0
  MENU_MAIN_MENU = 1
  MENU_CONTINUE = 2

  def update(self, events, game):
    for event in events:
      key = event.key
      if key == pygame.K_UP:
        self.model.prev_item()
      elif key == pygame.K_DOWN:
        self.model.next_item()
      elif key == pygame.K_ESCAPE:
        game.pop_mode()
        return False
      elif key == pygame.K_RETURN or key == pygame.K_SPACE:
        if self.model.selected_item == self.MENU_MAIN_MENU:
          game.reset_mode(game.MODE_MAIN_MENU)
          return False
        elif self.model.selected_item == self.MENU_CONTINUE:
          game.pop_mode()
          return False

    self.view.render()
    return True
