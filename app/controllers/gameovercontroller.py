import pygame
from app.controllers.controller import Controller

class GameOverController(Controller):

  def update(self, events, game):
    for event in events:
      key = event.key
      if key == pygame.K_ESCAPE or key == pygame.K_RETURN or key == pygame.K_SPACE:
        game.reset_mode(game.MODE_MAIN_MENU)
        return False

    self.view.render()
    return True
