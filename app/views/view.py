class View:
  def __init__(self, graphics, model):
    self.x = 0
    self.y = 0
    self.width = graphics.width
    self.height = graphics.height
    self.graphics = graphics
    self.model = model

  def set_pos(self, x, y):
    self.x = x
    self.y = y

  def render(self):
    pass
