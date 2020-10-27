class View:
  def __init__(self, graphics, model):
    self.x = 0
    self.y = 0
    self.width = graphics.screen_width
    self.height = graphics.screen_height
    self.graphics = graphics
    self.model = model

  def set_pos(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h

  def render(self):
    pass

  def update(self):
    pass
