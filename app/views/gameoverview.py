from app.views.modalview import ModalView
from app.views.menuview import MenuView
class GameOverView(ModalView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_title = self.graphics.load_image('data/img/title_game_over.png')
    self.menu_x = self.back_x + (self.img_back.get_width() - self.model.width) // 2
    self.menu_y = 66 + self.back_y + (self.img_back.get_height() - 66 - self.model.height) // 2
    self.menu_view = MenuView(graphics, model)
    self.menu_view.set_pos(self.menu_x, self.menu_y)

  def render(self):
    super().render()
    self.graphics.draw_image(self.img_title, self.menu_x, self.back_y + 12)
    self.menu_view.render()
