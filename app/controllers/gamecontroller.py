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
    model.data[model.start_addr] = Level.HEAD
    model.apple_addr = None
    self.python = Python(model.start_addr, model.free_cells)
    self.speed = 30 / 15
    self.delay = 0
    self.exit_active = False
    self.create_apple()

  def update(self, game, events):
    python = self.python
    if python.mode == Python.DEAD:
      if game.lives == 0:
        game.push_mode(game.MODE_GAME_OVER)
      else:
        self.reset_python()
      return
    elif python.mode == Python.OUT:
      if game.next_level():
        game.init_mode(game.MODE_START_LEVEL)
      else:
        game.init_mode(game.MODE_FINISH)
      return

    new_dir = python.dir

    for event in events:
      key = event.key
      if key == pygame.K_LEFT:
        new_dir = self.DIR_LEFT
      elif key == pygame.K_RIGHT:
        new_dir = self.DIR_RIGHT
      elif key == pygame.K_UP:
        new_dir = self.DIR_UP
      elif key == pygame.K_DOWN:
        new_dir = self.DIR_DOWN
      elif key == pygame.K_ESCAPE:
        game.push_mode(game.MODE_PAUSE)
        return

    if new_dir != python.dir:
      python.set_dir(new_dir)
      self.delay = 0

    if self.delay > 0:
      self.delay -= 1
      return

    if python.mode == Python.SHRINK or python.mode == Python.EXIT:
      self.delay += self.speed // 2
    else:
      self.delay += self.speed

    level = self.model

    tail_addr = python.get_tail_addr()
    python.move_tail()
    new_tail_addr = python.get_tail_addr()
    if (tail_addr != new_tail_addr):
      level.data[tail_addr] = Level.FIELD
    
    if python.mode == Python.MOVE or python.mode == Python.GROW:
      game.score += 1
      (head_dx, head_dy) = self.dirs[python.dir]
      self.view.head_dx = head_dx
      self.view.head_dy = head_dy
      head_addr = python.get_head_addr()
      level.data[head_addr] = Level.TAIL
      new_head_addr = head_addr + head_dy * level.width + head_dx
      data = level.data[new_head_addr]
      if data == Level.FIELD:
        python.move_head(new_head_addr)
        level.data[new_head_addr] = Level.HEAD
      elif data == Level.APPLE:
        python.move_head(new_head_addr)
        level.data[new_head_addr] = Level.HEAD
        game.apples += 1
        self.view.apples += 1
        python.set_mode(Python.GROW, 6)
        self.create_apple()
        game.score += 5
        game.audio.play_sfx('apple')
        if (self.view.apples == level.apple_count):
          self.exit_active = True
          self.view.exit_active = True
      elif data == Level.EXIT and self.exit_active:
        level.data[new_head_addr] = Level.TAIL
        python.set_mode(Python.EXIT, python.length)
        self.update_max_stats(game, python)
      else:
        python.set_mode(Python.SHRINK, python.length)
        self.update_max_stats(game, python)
        game.lives -= 1
        level.data[head_addr] = Level.HEAD
        level.data[level.apple_addr] = Level.FIELD
        game.audio.play_sfx('death')

    self.view.score = game.score
    self.view.length = python.length
    self.view.lives = game.lives
    python.update()
    self.view.render()

  def update_max_stats(self, game, python):
    if game.score > game.max_score:
      game.max_score = game.score
    length = python.length + 1
    if length > game.max_length:
      game.max_length = length

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
    self.model.data[self.model.start_addr] = Level.HEAD
    self.create_apple()
