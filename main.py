import pygame
from app.utils.config import Config
from app.game.game import Game
from app.game.level import Level
from app.graphics.graphics import Graphics
from app.audio.audio import Audio
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.models.menumodel import MenuModel

config = Config('game.ini')
w = int(config.window.width)
h = int(config.window.height)

audio = Audio()
audio.load_audio('music', 'data/audio/music.wav')
audio.load_audio('apple', 'data/audio/apple.wav')
audio.load_audio('death', 'data/audio/death.wav')

graphics = Graphics(w, h)

game = Game(graphics, audio)
game.init_mode(Game.MODE_MAIN_MENU)
clock = pygame.time.Clock()

audio.play_music('music')

while game.mode != Game.MODE_QUIT:
  events = pygame.event.get()
  controller_events = []
  for event in events:
    if event.type == pygame.QUIT:
      game.init_mode(Game.MODE_QUIT)
      break
    if event.type == pygame.KEYDOWN:
      controller_events.append(event)

  game.controller.update(game, controller_events)
  graphics.update()
  clock.tick(30)

pygame.quit()