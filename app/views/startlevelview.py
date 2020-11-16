from app.views.logoview import LogoView
from app.views.menuview import MenuView

class StartLevelView(LogoView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.level_num = 0
    self.apple_count = 0
    self.menu_view = MenuView(graphics, model)
    self.x = self.center_axis(0, self.width, self.menu_view.width)
    fp = graphics.get_font_params('green_light')
    offset_y = fp.get_lines_height(4)
    self.y = self.center_axis(
      self.logo_height, self.height,
      self.menu_view.height + offset_y)
    self.menu_view.set_pos(self.x, self.y + offset_y)

  def render(self):
    super().render()
    g = self.graphics
    g.set_font('white')
    str_level = 'LEVEL ' + str(self.level_num)
    str_level_width = g.font_params.get_str_width(str_level)
    str_level_x = self.center_axis(0, self.width, str_level_width)
    self.graphics.draw_text(str_level, str_level_x, self.y)
    g.set_font('green_light')
    str_apples = 'COLLECT ' + str(self.apple_count) + ' APPLES'
    str_apples_width = g.font_params.get_str_width(str_apples)
    str_apples_x = self.center_axis(0, self.width, str_apples_width)
    self.graphics.draw_text(str_apples, str_apples_x, self.y + g.font_params.get_lines_height(2))
    self.menu_view.render()
