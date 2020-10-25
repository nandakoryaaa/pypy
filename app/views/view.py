class View:
  def __init__(self, graphics, data):
    self.x = 0
    self.y = 0
    self.width = graphics.screen_width
    self.height = graphics.screen_height
    self.graphics = graphics
    self.data = data

  def set_pos(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h

  def render(self):
    pass

  def update(self):
    pass

class GameView(View):
  def render(self):
    y = 0
    x = 0
    offset = 0
    level = self.data
    for byte in level.data:
      if byte == level.WALL:
        self.graphics.draw_rect(x, y, 15, 15, (128,128,128))
      elif byte == level.FIELD:
        self.graphics.draw_rect(x, y, 15, 15, (128,255,128))
      elif byte == level.HEAD:
        self.graphics.draw_rect(x, y, 15, 15, (0,128,0))
      elif byte == level.TAIL:
        self.graphics.draw_rect(x, y, 15, 15, (0,156,0))
      elif byte == level.APPLE:
        self.graphics.draw_rect(x, y, 15, 15, (255,64,0))

      x += 16
      offset += 1
      if offset == level.line_length:
        offset = 0
        x = 0
        y += 16
