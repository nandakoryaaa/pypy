from app.views.view import View
from app.models.menuitem import MenuItem

class MenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.selector = self.model.get_selector()
    self.selector_dx = -self.selector.get_width() - 15
    self.width = 360
    self.arrow_left = self.graphics.load_image('data/img/arrow_left.png')
    self.arrow_right = self.graphics.load_image('data/img/arrow_right.png')

  def render(self):
    y = self.y
    for i in range(self.model.item_count):
      item = self.model.get_item(i)
      is_active = i == self.model.selected_item
      img = item.get_img(is_active)
      self.graphics.draw_image(img, self.x, y)
      self.render_control(item, y, is_active)
      if is_active:
        self.graphics.draw_image(self.selector, self.x + self.selector_dx, y)
      y += img.get_height() + 2

  def render_control(self, item, y, is_selected):
    if item.type == MenuItem.TYPE_SLIDER:
      self.graphics.draw_rect(self.x + self.width - 108 - 22, y + 8, 108, 32, (91,128,0))
      self.graphics.draw_rect(self.x + self.width - 104 - 22, y + 12, 100 * item.value, 24, (128,180,0))
      if is_selected:
        self.graphics.draw_image(self.arrow_left, self.x + self.width - 108 - 44, y + 16)
        self.graphics.draw_image(self.arrow_right, self.x + self.width - 18, y + 16)
