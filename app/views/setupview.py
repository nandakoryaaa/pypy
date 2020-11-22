from app.views.logoview import LogoView
from app.views.menuview import MenuView

class SetupView(LogoView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.level_num = 0
    self.apple_count = 0
    self.menu_view = MenuView(graphics, model)
    self.x = self.center_axis(0, self.width, self.menu_view.width)
    fp = graphics.get_font_params('green_light')
    offset_y = fp.get_lines_height(2)
    self.y = self.center_axis(
      self.logo_height, self.height,
      self.menu_view.height + offset_y
    )
    self.menu_view.set_pos(self.x, self.y + offset_y)

  def render(self):
    super().render()
    g = self.graphics
    g.set_font('white')
    str_title = 'SETUP'
    str_title_width = g.font_params.get_str_width(str_title)
    str_title_x = self.center_axis(0, self.width, str_title_width)
    self.graphics.draw_text(str_title, str_title_x, self.y)
    self.menu_view.render()
