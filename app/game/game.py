from app.game.level import Level
from app.graphics.graphics import Graphics
from app.views.gameview import GameView
from app.views.mainmenuview import MainMenuView
from app.controllers.gamecontroller import GameController
from app.controllers.mainmenucontroller import MainMenuController
from app.models.mainmenumodel import MainMenuModel

class Game:
	MODE_QUIT = 0
	MODE_MAIN_MENU = 1
	MODE_PLAY = 2
	MODE_NEXT_LEVEL = 3
	MODE_FINISH = 4
	MODE_OVER = 5
	MODE_OPTIONS = 6
	MODE_HALL_OF_FAME = 7

	def __init__(self, graphics):
		self.mode = self.MODE_QUIT
		self.controller = None
		self.graphics = graphics

	def init_mode(self, mode):
		if mode == self.MODE_MAIN_MENU:
			model = MainMenuModel(self.graphics, ('play', 'options', 'hall_of_fame', 'quit'))
			view = MainMenuView(self.graphics, model)
			self.controller = MainMenuController(view, model)
		elif mode == self.MODE_PLAY:
			file = open('data/level.txt', 'r')
			lines = file.readlines()
			level = Level(lines)
			view = GameView(self.graphics, level)
			self.controller = GameController(view, level)
		else:
			mode = self.MODE_QUIT
		self.mode = mode
