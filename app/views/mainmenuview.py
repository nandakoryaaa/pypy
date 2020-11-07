from app.views.view import View
from app.views.menuview import MenuView

class MainMenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/img/title_main.png')
    logo_height = self.img_logo.get_height()
    self.menu_view = MenuView(graphics, model)
    self.x = (self.graphics.width - self.menu_view.width) // 2
    self.y = logo_height + (self.graphics.height - logo_height - self.menu_view.height) // 2
    self.menu_view.set_pos(self.x, self.y)

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_logo, 0, 0)
    self.menu_view.render()

