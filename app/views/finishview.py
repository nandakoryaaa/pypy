from app.views.logoview import LogoView
from app.views.menuview import MenuView

class FinishView(LogoView):

  MSG_CONGRATS = 'CONGRATULATIONS!'
  MSG_FINISHED = 'YOU HAVE FINISHED THE GAME'
  MSG_MAX_LENGTH = 'MAX PYTHON LENGTH '
  MSG_APPLES = 'APPLES EATEN '

  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.length = 0
    self.apples = 0
    self.menu_view = MenuView(graphics, model)
    self.x = self.center_axis(0, self.width, self.menu_view.width)
    fp = graphics.get_font_params('green_light')
    offset_y = fp.get_lines_height(6)
    self.y = self.center_axis(
      self.logo_height, self.height,
      self.menu_view.height + offset_y)
    self.menu_view.set_pos(self.x, self.y + offset_y)
    self.step_y = fp.char_height + fp.line_spacing
    self.congrats_x = self.center_axis(0, self.width, fp.get_str_width(self.MSG_CONGRATS))
    self.finished_x = self.center_axis(0, self.width, fp.get_str_width(self.MSG_FINISHED))

  def render(self):
    super().render()
    g = self.graphics
    g.set_font('white')
    y = self.y
    self.graphics.draw_text(self.MSG_CONGRATS, self.congrats_x, y)
    y += self.step_y
    self.graphics.draw_text(self.MSG_FINISHED, self.finished_x, y)
    y += self.step_y * 2
    g.set_font('green_light')

    str_len = self.MSG_MAX_LENGTH + str(self.length)
    str_len_width = g.font_params.get_str_width(str_len)
    str_len_x = self.center_axis(0, self.width, str_len_width)
    self.graphics.draw_text(str_len, str_len_x, y)
    y += self.step_y

    str_apples = self.MSG_APPLES + str(self.apples)
    str_apples_width = g.font_params.get_str_width(str_apples)
    str_apples_x = self.center_axis(0, self.width, str_apples_width)
    self.graphics.draw_text(str_apples, str_apples_x, y)
    self.menu_view.render()
