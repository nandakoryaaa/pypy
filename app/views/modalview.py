from app.views.view import View

class ModalView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_shadow = graphics.load_image('data/img/modal_shadow.png')
    self.img_back = graphics.load_image('data/img/modal_back.png')
    self.x = (self.graphics.screen_width - self.img_shadow.get_width()) // 2
    self.y = (self.graphics.screen_height - self.img_shadow.get_height()) // 2
    self.back_x = (self.graphics.screen_width - self.img_back.get_width()) // 2
    self.back_y = (self.graphics.screen_height - self.img_back.get_height()) // 2
    self.shadow_drawn = False

  def render(self):
    if not self.shadow_drawn:
      self.graphics.draw_image(self.img_shadow, self.x, self.y)
      self.shadow_drawn = True

    self.graphics.draw_image(self.img_back, self.back_x, self.back_y)
