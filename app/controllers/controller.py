from random import randint
import pygame
from app.game.level import Level
from app.game.python import Python

class Controller:

  def __init__(self, view, model):
    self.view = view
    self.model = model

  def update(self, event):
    pass
