import pygame
from app.utils.config import Config
from app.game.level import Level
from app.graphics.graphics import Graphics
from app.views.view import GameView
from app.controllers.controller import GameController

config = Config('game.ini')

file = open('data/level.txt', 'r')
lines = file.readlines()
level = Level(lines)

graphics = Graphics(720, 480)

view = GameView(graphics, level)
controller = GameController(view, level)
clock = pygame.time.Clock()

is_playing = True
while is_playing:
  events = pygame.event.get()
  controller_events = []
  for event in events:
    if event.type == pygame.QUIT:
      is_playing = False
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        is_playing = False
        break
      controller_events.append(event)

  controller.update(controller_events)
  graphics.update()
  clock.tick(30)

pygame.quit()