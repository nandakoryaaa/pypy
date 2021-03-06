class View:

  MAX_TICKS = 30

  def __init__(self, graphics, model):
    self.x = 0
    self.y = 0
    self.width = graphics.width
    self.height = graphics.height
    self.graphics = graphics
    self.model = model
    self.ticks = 0

  def set_pos(self, x, y):
    self.x = x
    self.y = y

  def render(self):
    pass

  def center_axis(self, min, max, size):
    return min + (max - min - size) // 2

  def center_box(self, x0, y0, box_w, box_h, child_w, child_h):
    pos_x = self.center_axis(x0, x0 + box_w, child_w)
    pos_y = self.center_axis(y0, y0 + box_h, child_h)
    return (pos_x, pos_y)

  def update_ticks(self):
    self.ticks += 1
    if self.ticks >= self.MAX_TICKS:
      self.ticks = 0