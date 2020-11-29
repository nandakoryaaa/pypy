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
    self.free_cell_list = [0] * model.free_cells
    self.timer = 0
    self.apple_addr = None
    self.apple_timer = 0
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

    if self.apple_addr is not None:
      self.apple_timer -= 1
      if self.apple_timer == 0:
        self.remove_apple()
        self.create_apple()

    if self.delay > 0:
      self.delay -= 1
      return

    level = self.model
    is_shrinking = (python.mode == Python.SHRINK or python.mode == Python.EXIT)

    if is_shrinking:
      self.delay += self.speed // 2
    else:
      self.delay += self.speed

    if is_shrinking or python.mode == Python.MOVE:
      tail_addr = python.get_tail_addr()
      level.data[tail_addr] = Level.FIELD
      python.move_tail()
      if is_shrinking:
        self.view.update_apple_pos(python.get_tail_addr())

    if python.mode == Python.MOVE or python.mode == Python.GROW:
      game.score += 1
      (head_dx, head_dy) = self.dirs[python.dir]
      self.view.head_dx = head_dx
      self.view.head_dy = head_dy

      head_addr = python.get_head_addr()
      new_head_addr = head_addr + head_dy * level.width + head_dx
      data = level.data[new_head_addr]

      if data == Level.FIELD or data == Level.APPLE:
        level.data[head_addr] = Level.TAIL
        python.move_head(new_head_addr)
        level.data[new_head_addr] = Level.HEAD

        if data == Level.APPLE:
          game.apples += 1
          self.view.apples += 1
          if (self.view.apples == level.apple_count):
            self.exit_active = True
            self.view.exit_active = True
          python.set_mode(Python.GROW, level.growth + 1)
          self.create_apple()
          game.score += level.growth
          game.audio.play_sfx('apple')
      elif ((data == Level.EXIT and self.exit_active)
            or (python.length >= level.free_cells)):
        if data == Level.EXIT:
          level.data[head_addr] = Level.TAIL
          level.data[new_head_addr] = Level.TAIL
        python.set_mode(Python.EXIT, python.length)
        self.update_max_stats(game, python)
      else:
        python.set_mode(Python.SHRINK, python.length)
        self.update_max_stats(game, python)
        game.lives -= 1
        self.remove_apple()
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

  def remove_apple(self):
    self.model.data[self.apple_addr] = Level.FIELD
    self.apple_addr = None

  def create_apple(self):
    level = self.model
    free_count = level.get_free_cells(self.free_cell_list)
    if free_count == 0:
      return
    self.apple_addr = self.free_cell_list[randint(0, free_count - 1)]
    level.data[self.apple_addr] = Level.APPLE
    self.apple_timer = level.apple_timer
    self.view.update_apple_pos(self.apple_addr)

  def reset_python(self):
    head_addr = self.python.get_head_addr()
    self.model.data[head_addr] = Level.FIELD
    self.python.reset(self.model.start_addr)
    self.model.data[self.model.start_addr] = Level.HEAD
    self.create_apple()
