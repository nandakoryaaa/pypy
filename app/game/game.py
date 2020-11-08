from app.game.level import Level
from app.graphics.graphics import Graphics
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.views.pauseview import PauseView
from app.views.gameoverview import GameOverView
from app.views.enternameview import EnterNameView
from app.views.usertableview import UserTableView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.controllers.pausecontroller import PauseController
from app.controllers.gameovercontroller import GameOverController
from app.controllers.enternamecontroller import EnterNameController
from app.controllers.usertablecontroller import UserTableController
from app.models.menuitem import MenuItem
from app.models.menumodel import MenuModel

class Game:
  MODE_QUIT = 0
  MODE_MAIN_MENU = 1
  MODE_PLAY = 2
  MODE_NEXT_LEVEL = 3
  MODE_FINISH = 4
  MODE_GAME_OVER = 5
  MODE_OPTIONS = 6
  MODE_HALL_OF_FAME = 7
  MODE_PAUSE = 8
  MODE_ENTER_NAME = 9

  def __init__(self, graphics, audio):
    self.graphics = graphics
    self.audio = audio
    self.mode = self.MODE_QUIT
    self.controller = None
    self.lives = 0
    self.score = 0
    self.max_score = 0
    self.level = 0
    self.apples = 0
    self.max_length = 0
    self.user_name = 'NO NAME'
    self.user_table = None
    self.controller_stack = []

  def init_mode(self, mode):
    if mode == self.MODE_MAIN_MENU:
      model = MenuModel(self.graphics, (
        MenuItem(MenuItem.PLAY, 'PLAY'),
        MenuItem(MenuItem.OPTIONS, 'OPTIONS'),
        MenuItem(MenuItem.HALL_OF_FAME, 'HALL OF FAME'),
        MenuItem(MenuItem.QUIT, 'QUIT')
      ))
      view = MainMenuView(self.graphics, model)
      self.controller = MainMenuController(view, model)
    elif mode == self.MODE_PLAY:
      file = open('data/level.txt', 'r')
      lines = file.readlines()
      file.close()
      level = Level(lines)
      view = GameView(self.graphics, level)
      self.controller = GameController(view, level)
    elif mode == self.MODE_PAUSE:
      model = MenuModel(self.graphics, (
        MenuItem(MenuItem.MUSIC, 'MUSIC', MenuItem.TYPE_SLIDER, self.audio.music_volume),
        MenuItem(MenuItem.SOUND, 'SOUND', MenuItem.TYPE_SLIDER, self.audio.sfx_volume),
        MenuItem(MenuItem.MAIN_MENU, 'MAIN MENU'),
        MenuItem(MenuItem.CONTINUE, 'CONTINUE')
      ))
      view = PauseView(self.graphics, model)
      self.controller = PauseController(view, model)
    elif mode == self.MODE_GAME_OVER:
      model = MenuModel(self.graphics, (MenuItem(MenuItem.MAIN_MENU, 'MAIN MENU'),))
      view = GameOverView(self.graphics, model)
      self.controller = GameOverController(view, model)
    elif mode == self.MODE_ENTER_NAME:
      model = MenuModel(self.graphics, (MenuItem(MenuItem.CONTINUE, 'CONTINUE'),))
      view = EnterNameView(self.graphics, model)
      view.user_name = self.user_name
      self.controller = EnterNameController(view, model)
    elif mode == self.MODE_HALL_OF_FAME:
      menu_model = MenuModel(self.graphics, (MenuItem(MenuItem.MAIN_MENU, 'MAIN MENU'),))
      view = UserTableView(self.graphics, self.user_table.table, menu_model)
      self.controller = UserTableController(view, menu_model)
    else:
      mode = self.MODE_QUIT
    self.mode = mode

  def push_mode(self, mode):
    self.controller_stack.append((self.mode, self.controller))
    self.init_mode(mode)

  def pop_mode(self):
    (mode, controller) = self.controller_stack.pop()
    self.mode = mode
    self.controller = controller

  def reset_mode(self, mode):
    self.controller_stack = []
    self.init_mode(mode)
