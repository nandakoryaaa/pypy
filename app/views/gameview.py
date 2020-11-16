import math
from app.views.view import View

class GameView(View):

  COLOR_EYE = (255,180,0)
  COLOR_PUPIL = (0,0,0)
  COLOR_WALL = (128,128,128)
  COLOR_FIELD = (128,255,128)
  COLOR_HEAD = (0,128,0)
  COLOR_TAIL = (0,156,0)
  COLOR_APPLE = (255,64,0)

  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_esc_menu = graphics.load_image('data/img/esc_menu.png')
    self.img_life = graphics.load_image('data/img/life.png')
    self.img_life_lost = graphics.load_image('data/img/life_lost.png')
    self.img_score = graphics.load_image('data/img/score.png')
    self.img_length = graphics.load_image('data/img/length.png')
    self.img_apples = graphics.load_image('data/img/apples.png')
    level_w = self.model.width + 2
    level_h = self.model.height + 2

    fp = graphics.get_font_params('digits_gradient')
    offset_y = fp.char_height
    actual_height = self.height - offset_y

    cell_size = self.width // level_w
    cell_size2 = actual_height // level_h

    if (cell_size2 < cell_size):
      cell_size = cell_size2

    self.level_x = cell_size + self.center_axis(0, self.width, cell_size * level_w)
    self.level_y = offset_y + cell_size + self.center_axis(0, actual_height, cell_size * level_h)
    self.cell_size = cell_size
    self.exit_active = False
    self.score = 0
    self.apples = 0
    self.length = 0
    self.lives = 0
    self.head_dx = 0
    self.head_dy = 0
    self.apple_x = 0
    self.apple_y = 0
    self.pupil_size = cell_size // 5
    self.eye_size = self.pupil_size * 2

  def render(self):
    self.update_ticks()

    self.graphics.fill((0,0,0))
    self.graphics.set_font('digits_gradient')

    self.graphics.draw_image(self.img_score, 10, 18)
    self.graphics.draw_text(str(self.score), 119, 5)

    self.graphics.draw_image(self.img_length, 391, 18)
    self.graphics.draw_text(str(self.length), 519, 5)

    self.graphics.draw_image(self.img_apples, 719, 18)
    self.graphics.draw_text(str(self.apples), 847, 5)

    x = 1011
    for i in range (3 - self.lives):
      self.graphics.draw_image(self.img_life_lost, x, 13)
      x += 33
    for i in range (self.lives):
      self.graphics.draw_image(self.img_life, x, 13)
      x += 33

    self.graphics.draw_image(self.img_esc_menu, 1183, 23)

    x = self.level_x
    y = self.level_y
    cell_size = self.cell_size - 1
    offset = 0
    level = self.model
    for byte in level.data:
      if byte == level.WALL:
        self.graphics.draw_rect(x, y, cell_size, cell_size, self.COLOR_WALL)
      elif byte == level.FIELD:
        self.graphics.draw_rect(x, y, cell_size, cell_size, self.COLOR_FIELD)
      elif byte == level.HEAD:
        self.graphics.draw_rect(x, y, cell_size, cell_size, self.COLOR_HEAD)
        self.draw_eyes(x, y)
      elif byte == level.TAIL:
        self.graphics.draw_rect(x, y, cell_size, cell_size, self.COLOR_TAIL)
      elif byte == level.APPLE:
        self.draw_pulse_box(x, y, self.COLOR_APPLE)
      elif byte == level.EXIT:
        if self.exit_active:
          self.draw_pulse_box(x, y, self.COLOR_WALL)
        else: 
          self.graphics.draw_rect(x, y, cell_size, cell_size, self.COLOR_WALL)
      x += self.cell_size
      offset += 1
      if offset == level.width:
        offset = 0
        x = self.level_x
        y += self.cell_size

  def update_apple_pos(self, addr):
    self.apple_x = self.level_x + addr % self.model.width * self.cell_size
    self.apple_y = self.level_y + addr // self.model.width * self.cell_size

  def draw_pulse_box(self, x, y, color):
    cs = self.cell_size
    self.graphics.draw_rect(x, y, cs - 1, cs - 1, self.COLOR_FIELD)
    half_apple_size = cs // 2
    progress = math.pi * 4 * self.ticks / self.MAX_TICKS
    apple_size = half_apple_size + int(half_apple_size * (1 + math.cos(progress)) / 2)
    offset = (cs - apple_size) // 2
    self.graphics.draw_rect(x + offset, y + offset, apple_size, apple_size, color)

  def draw_eyes(self, x, y):
    pupil_size = self.pupil_size

    if pupil_size < 1:
      return

    eye_size = self.eye_size
    eye_dist = self.cell_size - 1 - eye_size
    eye_x = x
    eye_y = y
    eye_x2 = x + eye_dist
    eye_y2 = y

    if self.head_dx > 0:
      eye_x += eye_dist
      eye_y2 += eye_dist
    elif self.head_dx < 0:
      eye_x2 = x
      eye_y2 += eye_dist
    elif self.head_dy > 0:
      eye_y += eye_dist
      eye_y2 += eye_dist

    self.graphics.draw_rect(eye_x, eye_y, eye_size, eye_size, self.COLOR_EYE)
    self.graphics.draw_rect(eye_x2, eye_y2, eye_size, eye_size, self.COLOR_EYE)
    pupil_x = pupil_y = pupil_size // 2
    if self.apple_x > x:
      pupil_x = eye_size - pupil_size
    elif self.apple_x < x:
      pupil_x = 0
    if self.apple_y > y:
      pupil_y = eye_size - pupil_size
    elif self.apple_y < y:
      pupil_y = 0
    self.graphics.draw_rect(eye_x + pupil_x, eye_y + pupil_y, pupil_size, pupil_size, self.COLOR_PUPIL)
    self.graphics.draw_rect(eye_x2 + pupil_x, eye_y2 + pupil_y, pupil_size, pupil_size, self.COLOR_PUPIL)
