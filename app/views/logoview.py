from app.views.view import View

class LogoView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/img/title_main.png')
    self.img_logo_tile = graphics.load_image('data/img/title_main_tile.png')
    self.logo_width = self.img_logo.get_width()
    self.logo_height = self.img_logo.get_height()
    self.logo_tile_width = self.img_logo_tile.get_width()
    self.logo_x = self.center_axis(0, self.width, self.logo_width)

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_logo, self.logo_x, 0)
    left_side = self.logo_x
    right_side = self.logo_x + self.logo_width
    while left_side > 0:
      left_side -= self.logo_tile_width
      self.graphics.draw_image(self.img_logo_tile, left_side, 0)
      self.graphics.draw_image(self.img_logo_tile, right_side, 0)
      right_side += self.logo_tile_width
      


