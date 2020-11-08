from app.views.view import View
from app.models.menuitem import MenuItem

class MenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.selector = graphics.load_image('data/img/menu_select.png')
    self.selector_dx = -self.selector.get_width() - 15
    self.width = 0
    self.control_x = 0
    self.graphics.set_font('green_dark')
    fp = self.graphics.font_params
    for item in model.item_list:
      w = fp.get_str_width(item.text)
      if w > self.width:
        self.width = w
      if item.type == MenuItem.TYPE_SLIDER and w > self.control_x:
        self.control_x = w
    self.width += self.selector_dx
    self.height = fp.get_lines_height(model.item_count)
    self.arrow_left = self.graphics.load_image('data/img/arrow_left.png')
    self.arrow_right = self.graphics.load_image('data/img/arrow_right.png')

  def render(self):
    y = self.y
    self.graphics.set_font('green_dark')
    for i in range(self.model.item_count):
      item = self.model.get_item(i)
      is_active = i == self.model.selected_item
      if is_active:
        self.graphics.set_font('green_light')
      else:
        self.graphics.set_font('green_dark')
      self.graphics.draw_text(item.text, self.x, y)
      self.render_control(item, y, is_active)
      if is_active:
        self.graphics.draw_image(self.selector, self.x + self.selector_dx, y)
      y += self.graphics.font_params.char_height + 10

  def render_control(self, item, y, is_selected):
    if item.type == MenuItem.TYPE_SLIDER:
      self.graphics.draw_rect(self.x + self.control_x + 32, y + 6, 108, 32, (91,128,0))
      self.graphics.draw_rect(self.x + self.control_x + 36, y + 10, 100 * item.value, 24, (128,180,0))
      if is_selected:
        self.graphics.draw_image(self.arrow_left, self.x + self.control_x + 10, y + 14)
        self.graphics.draw_image(self.arrow_right, self.x + self.control_x + 144, y + 14)
