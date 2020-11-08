from app.views.logoview import LogoView
from app.views.menuview import MenuView

class MainMenuView(LogoView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.menu_view = MenuView(graphics, model)
    self.x = (self.graphics.width - self.menu_view.width) // 2
    self.y = self.logo_height + (self.graphics.height - self.logo_height - self.menu_view.height) // 2
    self.menu_view.set_pos(self.x, self.y)

  def render(self):
    super().render()
    self.menu_view.render()

