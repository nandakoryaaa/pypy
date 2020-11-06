from app.views.view import View
from app.views.menuview import MenuView

class MainMenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/img/title_main.png').convert()
    logo_height = self.img_logo.get_height()
    self.menu_x = (self.graphics.screen_width - self.model.width) // 2
    self.menu_y = logo_height + (self.graphics.screen_height - logo_height - self.model.height) // 2
    self.menu_view = MenuView(graphics, model)
    self.menu_view.set_pos(self.menu_x, self.menu_y)

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_logo, 0, 0)
    self.menu_view.render()

