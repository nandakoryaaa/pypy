from app.views.view import View

class GameView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_stats = graphics.load_image('data/graphics/stats.png')

    screen_w = self.graphics.screen_width
    screen_h = self.graphics.screen_height - self.img_stats.get_height()
    level_w = self.model.width + 2
    level_h = self.model.height + 2

    cell_size = screen_w // level_w
    cell_size2 = screen_h // level_h

    if (cell_size2 < cell_size):
      cell_size = cell_size2

    self.level_x = cell_size + (screen_w - cell_size * level_w) // 2
    self.level_y = cell_size + self.img_stats.get_height() + (screen_h - cell_size * level_h) // 2
    self.cell_size = cell_size
    self.score = 0
    self.length = 0

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_stats, 0, 0)
    self.graphics.draw_text(str(self.score), 145, 5)
    self.graphics.draw_text(str(self.length), 565, 5)

    x = self.level_x
    y = self.level_y
    cell_size = self.cell_size - 1
    offset = 0
    level = self.model
    for byte in level.data:
      if byte == level.WALL:
        self.graphics.draw_rect(x, y, cell_size, cell_size, (128,128,128))
      elif byte == level.FIELD:
        self.graphics.draw_rect(x, y, cell_size, cell_size, (128,255,128))
      elif byte == level.HEAD:
        self.graphics.draw_rect(x, y, cell_size, cell_size, (0,128,0))
      elif byte == level.TAIL:
        self.graphics.draw_rect(x, y, cell_size, cell_size, (0,156,0))
      elif byte == level.APPLE:
        self.graphics.draw_rect(x, y, cell_size, cell_size, (255,64,0))

      x += cell_size + 1
      offset += 1
      if offset == level.width:
        offset = 0
        x = self.level_x
        y += cell_size + 1
