from app.views.view import View

class GameView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_esc_menu = graphics.load_image('data/img/esc_menu.png')
    self.img_life = graphics.load_image('data/img/life.png')
    self.img_life_lost = graphics.load_image('data/img/life_lost.png')

    screen_w = self.graphics.width
    screen_h = self.graphics.height - 50
    level_w = self.model.width + 2
    level_h = self.model.height + 2

    cell_size = screen_w // level_w
    cell_size2 = screen_h // level_h

    if (cell_size2 < cell_size):
      cell_size = cell_size2

    self.level_x = cell_size + (screen_w - cell_size * level_w) // 2
    self.level_y = cell_size + 50 + (screen_h - cell_size * level_h) // 2
    self.cell_size = cell_size
    self.score = 0
    self.length = 0
    self.lives = 0

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.set_font('green_dark')
    self.graphics.draw_text('SCORE', 10, 5)
    self.graphics.draw_text('LENGTH', 10+36*12, 5)
    self.graphics.set_font('digits_gradient')
    self.graphics.draw_text(str(self.score), 10+36*6, 5)
    self.graphics.draw_text(str(self.length), 10+36*19, 5)

    x = 10+36*26
    for i in range (3 - self.lives):
      self.graphics.draw_image(self.img_life_lost, x, 6)
      x += 46
    for i in range (self.lives):
      self.graphics.draw_image(self.img_life, x, 6)
      x += 46

    self.graphics.draw_image(self.img_esc_menu, 1126, 18)

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
