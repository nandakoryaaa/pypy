import pygame
from app.utils.config import Config
from app.game.game import Game
from app.game.level import Level
from app.graphics.graphics import Graphics
from app.graphics.fontparams import FontParams
from app.audio.audio import Audio
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.models.menumodel import MenuModel

config = Config('game.ini')

audio = Audio()
audio.load_audio('music', 'data/audio/music.wav')
audio.load_audio('apple', 'data/audio/apple.wav')
audio.load_audio('death', 'data/audio/death.wav')

graphics = Graphics(int(config.window.width), int(config.window.height))
graphics.load_font_img('data/fonts/font.png')
graphics.add_font_params('digits_gradient', FontParams(0,0,36,44,4,16,10,'0123456789'))
graphics.add_font_params('green_dark', FontParams(0,44,36,44,4,16,10,'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!.'))
graphics.add_font_params('green_light', FontParams(0,44*5,36,44,4,16,10,'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!.'))
graphics.add_font_params('white', FontParams(0,44*9,36,44,4,16,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ!.'))

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