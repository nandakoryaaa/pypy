from random import randint
import pygame
from app.controllers.controller import Controller
from app.game.level import Level
from app.game.python import Python

class GameController(Controller):

  DIR_LEFT = 0
  DIR_UP = 1
  DIR_RIGHT = 2
  DIR_DOWN = 3
  dirs = ((-1,0), (0,-1), (1,0), (0,1))

  def __init__(self, view, model):
    super().__init__(view, model)
    self.python = Python(model.start_addr, model.free_cells)
    model.data[model.start_addr] = Level.HEAD
    self.speed = 30 / 15
    self.delay = 0
    model.apple_addr = None
    self.create_apple()

  def update(self, game, events):
    python = self.python
    if python.mode == Python.DEAD:
      if game.lives == 0:
        game.push_mode(game.MODE_GAME_OVER)
      else:
        self.reset_python()
      return

    dir = python.dir

    for event in events:
      key = event.key
      if key == pygame.K_LEFT:
        python.set_dir(self.DIR_LEFT)
      elif key == pygame.K_RIGHT:
        python.set_dir(self.DIR_RIGHT)
      elif key == pygame.K_UP:
        python.set_dir(self.DIR_UP)
      elif key == pygame.K_DOWN:
        python.set_dir(self.DIR_DOWN)
      elif key == pygame.K_ESCAPE:
        game.push_mode(game.MODE_PAUSE)
        return

    if self.delay > 0:
      self.delay -= 1
      return

    self.delay += self.speed
    level = self.model

    tail_addr = python.get_tail_addr()
    python.move_tail()
    new_tail_addr = python.get_tail_addr()

    level.data[tail_addr] = Level.FIELD
    level.data[new_tail_addr] = Level.TAIL
    (head_dx, head_dy) = self.dirs[python.dir]

    head_addr = python.get_head_addr()

    if python.mode == Python.MOVE or python.mode == Python.GROW:
      game.score += 1
      new_head_addr = head_addr + head_dy * level.width + head_dx

      if level.data[new_head_addr] == Level.APPLE:
        game.apples += 1
        python.set_mode(Python.GROW, 6)
        self.create_apple()
        game.score += 5
        game.audio.play_sfx('apple')
      elif level.data[new_head_addr] != Level.FIELD:
        python.set_mode(Python.SHRINK, python.length)
        game.lives -= 1
        if game.score > game.max_score:
          game.max_score = game.score
        if python.length > game.max_length:
          game.max_length = python.length
        new_head_addr = head_addr
        level.data[level.apple_addr] = Level.FIELD
        game.audio.play_sfx('death')

      python.move_head(new_head_addr)
      level.data[head_addr] = Level.TAIL
      head_addr = new_head_addr

    level.data[head_addr] = Level.HEAD

    self.view.score = game.score
    self.view.length = python.length
    self.view.lives = game.lives
    self.view.head_dx = head_dx
    self.view.head_dy = head_dy
    python.update()
    self.view.render()

  def create_apple(self):
    level = self.model
    apple_addr = None
    while(True):
      apple_addr = randint(level.width + 2, len(level.data) - level.width - 2)
      if level.data[apple_addr] == Level.FIELD:
        break

    level.data[apple_addr] = Level.APPLE
    level.apple_addr = apple_addr
    self.view.update_apple_pos(apple_addr)

  def reset_python(self):
    head_addr = self.python.get_head_addr()
    self.model.data[head_addr] = Level.FIELD
    self.python.reset(self.model.start_addr)
    self.create_apple()
