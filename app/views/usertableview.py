from app.views.logoview import LogoView
from app.views.menuview import MenuView

class UserTableView(LogoView):

  MSG = 'HALL_OF FAME'

  def __init__(self, graphics, model, menu_model):
    super().__init__(graphics, model)
    self.menu_view = MenuView(graphics, menu_model)
    fp = graphics.font_params
    self.title_x = self.center_axis(0, self.width, fp.get_str_width(self.MSG))
    self.x = self.center_axis(0, self.width, fp.get_len_width(28))
    self.y = self.center_axis(0, self.height, fp.get_lines_height(14, 4))
    self.menu_view.x = self.center_axis(0, self.width, self.menu_view.width)

  def render(self):
    super().render()
    g = self.graphics
    g.set_font('white')
    fp = g.font_params
    y = self.y
    step_y = fp.char_height + 4
    step_x = fp.char_width + fp.char_spacing
    g.draw_text(self.MSG, self.title_x, y)
    y += step_y + step_y
    i = 1
    for user_data in self.model:
      x = self.x
      g.set_font('green_dark')
      s = str(i) + '.'
      if i < 10:
        x += step_x
      g.draw_text(s, x, y)
      x = self.x + step_x * 3
      s = user_data.name
      g.set_font('green_light')
      g.draw_text(s, x, y)
      count = len(s)
      x += step_x * count
      g.set_font('green_dark')
      score = str(user_data.score)
      target_count = 18 + 6 - len(score)
      while count < target_count:
        g.draw_text('.', x, y)
        count += 1
        x += step_x
      g.set_font('digits_gradient')
      g.draw_text(str(user_data.score), x, y)    
      y += step_y
      i += 1

    self.menu_view.y = y + step_y
    self.menu_view.render()
