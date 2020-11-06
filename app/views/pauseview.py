from app.views.modalview import ModalView
from app.views.menuview import MenuView

class PauseView(ModalView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_title = graphics.load_image('data/img/title_pause.png')
    self.img_esc = graphics.load_image('data/img/modal_esc_x.png')
    self.menu_view = MenuView(graphics, model)
    self.menu_x = self.back_x + (self.img_back.get_width() - self.model.width) // 2
    self.menu_y = 66 + self.back_y + (self.img_back.get_height() - 66 - self.model.height) // 2
    self.menu_view.set_pos(self.menu_x, self.menu_y)

  def render(self):
    super().render()
    self.graphics.draw_image(self.img_title, self.menu_x, self.back_y + 12)
    self.graphics.draw_image(self.img_esc, self.back_x + 378, self.back_y + 21)
    self.menu_view.render()
