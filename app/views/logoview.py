from app.views.view import View

class LogoView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/img/title_main.png')
    self.logo_height = self.img_logo.get_height()


  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_logo, 0, 0)


