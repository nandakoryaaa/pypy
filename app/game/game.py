from app.game.level import Level
from app.graphics.graphics import Graphics
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.views.pauseview import PauseView
from app.views.gameoverview import GameOverView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.controllers.pausecontroller import PauseController
from app.controllers.gameovercontroller import GameOverController
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

	def __init__(self, graphics):
		self.mode = self.MODE_QUIT
		self.controller = None
		self.graphics = graphics
		self.score = 0
		self.lives = 0
		self.controller_stack = []

	def init_mode(self, mode):
		if mode == self.MODE_MAIN_MENU:
			model = MenuModel(self.graphics, ('menu_play', 'menu_options', 'menu_hall_of_fame', 'menu_quit'))
			view = MainMenuView(self.graphics, model)
			self.controller = MainMenuController(view, model)
		elif mode == self.MODE_PLAY:
			file = open('data/level.txt', 'r')
			lines = file.readlines()
			level = Level(lines)
			view = GameView(self.graphics, level)
			self.controller = GameController(view, level)
		elif mode == self.MODE_PAUSE:
			model = MenuModel(self.graphics, ('pause_menu_sound', 'pause_menu_main_menu', 'pause_menu_continue'))
			view = PauseView(self.graphics, model)
			self.controller = PauseController(view, model)
		elif mode == self.MODE_GAME_OVER:
			model = MenuModel(self.graphics, ('pause_menu_main_menu',))
			view = GameOverView(self.graphics, model)
			self.controller = GameOverController(view, model)
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