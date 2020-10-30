from app.views.modalview import ModalView

class PauseView(ModalView):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_title = graphics.load_image('data/img/title_pause.png')
    self.img_esc = graphics.load_image('data/img/modal_esc_x.png')
    self.menu_x = self.back_x + (self.img_back.get_width() - self.model.width) // 2
    self.menu_y = 66 + self.back_y + (self.img_back.get_height() - 66 - self.model.item_height * self.model.item_count) // 2
    self.selector = self.model.get_selector()
    self.selector_x = self.menu_x - self.selector.get_width() - 15

  def render(self):
    super().render()
    self.graphics.draw_image(self.img_title, self.menu_x, self.back_y + 12)
    self.graphics.draw_image(self.img_esc, self.back_x + 378, self.back_y + 21)
    for i in range(self.model.item_count):
      y = self.menu_y + i * self.model.item_height
      item = self.model.get_item(i)
      self.graphics.draw_image(item, self.menu_x, y)
      if i == self.model.selected_item:
        self.graphics.draw_image(self.selector, self.selector_x, y)

