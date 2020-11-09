from app.views.view import View
from app.views.menuview import MenuView

class EnterNameView(View):

  MSG = 'ENTER YOUR NAME'

  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/img/title_main.png')
    logo_height = self.img_logo.get_height()
    self.menu_view = MenuView(graphics, model)
    fp = graphics.font_params
    self.prompt_x = (graphics.width - fp.get_str_width(self.MSG)) // 2
    self.prompt_y = logo_height + 2 * fp.char_height
    self.x = (graphics.width - self.menu_view.width) // 2
    self.y = logo_height + (graphics.height - logo_height - self.menu_view.height) // 2
    self.menu_view.set_pos(self.x, self.y + 100)
    self.user_name = ''

  def render(self):
    self.update_ticks()
    if self.ticks >= self.MAX_TICKS:
      self.ticks = 0

    g = self.graphics
    g.fill((0,0,0))
    g.draw_image(self.img_logo, 0, 0)
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
