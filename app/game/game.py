from app.game.level import Level
from app.graphics.graphics import Graphics
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.views.pauseview import PauseView
from app.views.gameoverview import GameOverView
from app.views.finishview import FinishView
from app.views.startlevelview import StartLevelView
from app.views.enternameview import EnterNameView
from app.views.usertableview import UserTableView
from app.views.setupview import SetupView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.controllers.pausecontroller import PauseController
from app.controllers.gameovercontroller import GameOverController
from app.controllers.startlevelcontroller import StartLevelController
from app.controllers.enternamecontroller import EnterNameController
from app.controllers.usertablecontroller import UserTableController
from app.controllers.setupcontroller import SetupController
from app.models.menuitem import MenuItem
from app.models.menumodel import MenuModel

class Game:
  MODE_QUIT = 0
  MODE_MAIN_MENU = 1
  MODE_PLAY = 2
  MODE_START_LEVEL = 3
  MODE_FINISH = 4
  MODE_GAME_OVER = 5
  MODE_SETUP = 6
  MODE_HALL_OF_FAME = 7
  MODE_PAUSE = 8
  MODE_ENTER_NAME = 9
  
  def __init__(self, config, graphics, audio):
    self.config = config
    self.graphics = graphics
    self.audio = audio
    self.mode = self.MODE_QUIT
    self.controller = None
    self.level_list = None
    self.level_num = 0
    self.lives = 0
    self.score = 0
    self.max_score = 0
    self.apples = 0
    self.max_length = 0
    self.user_name = 'NO NAME'
    self.user_table = None
    self.controller_stack = []
    self.load_level_list(config)
    self.main_menu_model = MenuModel(graphics, (MenuItem(MenuItem.MAIN_MENU, 'MAIN MENU'),))

  def set_fullscreen(self, b):
    self.graphics.set_display_mode(1280, 720, b)

  def load_level_list(self, config):
    levels = config.game.levels.split(',')
    self.level_list = []
    for level_id in levels:
      level_id = level_id.strip()
      self.level_list.append(level_id)

  def load_level(self, num):
    level_id = self.level_list[num]
    level_config = self.config.get_section(level_id)
    file = open('data/' + level_config.file, 'r')
    lines = file.readlines()
    file.close()
    level = Level(lines)
    level.apple_count = int(level_config.apple_count)
    level.growth = int(level_config.growth)
    fps = int(self.config.game.fps)
    level.timer = int(level_config.timer) * fps
    level.apple_timer = int(level_config.apple_timer) * fps
    return level

  def init_mode(self, mode):
    if mode == self.MODE_MAIN_MENU:
      self.audio.play_music('music')
      model = MenuModel(self.graphics, (
        MenuItem(MenuItem.PLAY, 'PLAY'),
        MenuItem(MenuItem.SETUP, 'SETUP'),
        MenuItem(MenuItem.HALL_OF_FAME, 'HALL OF FAME'),
        MenuItem(MenuItem.QUIT, 'QUIT')
      ))
      view = MainMenuView(self.graphics, model)
      self.controller = MainMenuController(view, model)
    elif mode == self.MODE_START_LEVEL:
      level_id = self.level_list[self.level_num]
      level_config = self.config.get_section(level_id)
      model = MenuModel(self.graphics, (MenuItem(MenuItem.MAIN_MENU, 'PLAY'),))
      view = StartLevelView(self.graphics, model)
      view.level_num = self.level_num + 1
      view.apple_count = int(level_config.apple_count)
      self.controller = StartLevelController(view, model)
    elif mode == self.MODE_PLAY:
      level = self.load_level(self.level_num)
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
    elif mode == self.MODE_FINISH:
      self.audio.play_music('finish')
      view = FinishView(self.graphics, self.main_menu_model)
      view.length = self.max_length
      view.apples = self.apples
      self.controller = GameOverController(view, self.main_menu_model)
    elif mode == self.MODE_GAME_OVER:
      view = GameOverView(self.graphics, self.main_menu_model)
      self.controller = GameOverController(view, self.main_menu_model)
    elif mode == self.MODE_ENTER_NAME:
      model = MenuModel(self.graphics, (MenuItem(MenuItem.CONTINUE, 'CONTINUE'),))
      view = EnterNameView(self.graphics, model)
      view.user_name = self.user_name
      self.controller = EnterNameController(view, model)
    elif mode == self.MODE_HALL_OF_FAME:
      view = UserTableView(self.graphics, self.user_table.table, self.main_menu_model)
      self.controller = UserTableController(view, self.main_menu_model)
    elif mode == self.MODE_SETUP:
      model = MenuModel(self.graphics, (
        MenuItem(MenuItem.SCREEN_SIZE, 'SCREEN SIZE', MenuItem.TYPE_LIST,
          ('800 X 600', '1024 X 768', '1280 X 720', '1366 X 768', '1920 X 1080'),
          self.graphics.display_mode_num
        ),
        MenuItem(MenuItem.FULLSCREEN, 'FULLSCREEN', MenuItem.TYPE_LIST, ('YES','NO'), 0 if self.graphics.fullscreen else 1),
        MenuItem(MenuItem.MUSIC, 'MUSIC', MenuItem.TYPE_SLIDER, self.audio.music_volume),
        MenuItem(MenuItem.SOUND, 'SOUND', MenuItem.TYPE_SLIDER, self.audio.sfx_volume),
        MenuItem(MenuItem.SAVE, 'APPLY AND SAVE CHANGES'),
        MenuItem(MenuItem.CANCEL, 'CANCEL')
      ))
      view = SetupView(self.graphics, model)
      controller = SetupController(view, model)
      controller.display_mode_num = self.graphics.display_mode_num
      controller.fullscreen = self.graphics.fullscreen
      self.controller = controller
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

  def next_level(self):
    if self.level_num >= len(self.level_list) - 1:
      return False
    self.level_num += 1
    return True
