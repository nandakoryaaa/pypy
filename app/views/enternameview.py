from app.views.logoview import LogoView
from app.views.menuview import MenuView

class EnterNameView(LogoView):

  MSG = 'ENTER YOUR NAME'

  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.menu_view = MenuView(graphics, model)
    fp = graphics.get_font_params('white')
    self.prompt_x = self.center_axis(0, self.width, fp.get_str_width(self.MSG))
    self.prompt_y = self.logo_height + 2 * fp.char_height
    self.x = self.center_axis(0, self.width, self.menu_view.width)
    self.y = self.center_axis(self.logo_height, graphics.height, self.menu_view.height)
    self.menu_view.set_pos(self.x, self.y + 100)
    self.user_name = ''

  def render(self):
    super().render()
    self.update_ticks()

    g = self.graphics
    g.set_font('green_light')
    fp = g.font_params
    y = self.prompt_y
    g.draw_text(self.MSG, self.prompt_x, y)
    y += fp.char_height * 2
    g.draw_rect(self.prompt_x - fp.char_spacing, y - fp.char_spacing,
		 fp.get_str_width(self.MSG) + fp.char_spacing * 2, fp.char_height + fp.char_spacing * 2, (30,80,0))
    g.set_font('white')
    g.draw_text(self.user_name, self.prompt_x, y)
    if self.ticks <= self.MAX_TICKS // 2:
      g.draw_rect(self.prompt_x + fp.get_str_width(self.user_name) + fp.char_spacing, y + fp.char_height - 8,
		fp.char_width / 2, 8, (255,255,255))

    self.menu_view.render()
