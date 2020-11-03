import pygame
from app.controllers.controller import Controller

class MainMenuController(Controller):
  MENU_PLAY = 0
  MENU_OPTIONS = 1
  MENU_HALL_OF_FAME = 2
  MENU_QUIT = 3

  def __init__(self, view, model):
    super().__init__(view, model)

  def update(self, events, game):
    for event in events:
      key = event.key
      if key == pygame.K_UP:
        self.model.prev_item()
        game.audio.play_sfx('apple')
      elif key == pygame.K_DOWN:
        self.model.next_item()
        game.audio.play_sfx('apple')
      elif key == pygame.K_RETURN or key == pygame.K_SPACE:
        if self.model.selected_item == self.MENU_PLAY:
          game.score = 0
          game.lives = 3
          game.init_mode(game.MODE_PLAY)
          return False
        elif self.model.selected_item == self.MENU_QUIT:
          game.init_mode(game.MODE_QUIT)
          return False

    self.view.render()
    return True

