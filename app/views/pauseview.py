from app.views.modalview import ModalView
from app.views.menuview import MenuView

class PauseView(ModalView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_esc = graphics.load_image('data/img/modal_esc_x.png')
    self.menu_view = MenuView(graphics, model)
    self.menu_x = self.back_x + (self.img_back.get_width() - self.menu_view.width) // 2
    self.menu_y = 66 + self.back_y + (self.img_back.get_height() - 66 - self.menu_view.height) // 2
    self.menu_view.set_pos(self.menu_x, self.menu_y)

  def render(self):
    super().render()
    self.graphics.draw_image(self.img_esc, self.back_x + 440, self.back_y + 11)
    self.graphics.set_font('white')
    self.graphics.draw_text('PAUSE', self.menu_x + self.menu_view.selector_dx, self.back_y + 12)
    self.menu_view.render()
