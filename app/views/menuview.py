from app.views.view import View
from app.models.menuitem import MenuItem

class MenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.selector = graphics.load_image('data/img/menu_select.png')
    self.selector_dx = -self.selector.get_width() - 15
    self.width = 0
    self.control_x = 0
    self.fp = self.graphics.get_font_params('green_dark')
    for item in model.item_list:
      w = self.fp.get_str_width(item.text)
      if (item.type == MenuItem.TYPE_SLIDER or item.type == MenuItem.TYPE_LIST) and w > self.control_x:
        self.control_x = w
      if item.type == MenuItem.TYPE_LIST:
        max_w = 0
        for str in item.value:
          str_len = len(str)
          if str_len > max_w:
            max_w = str_len
        w += self.fp.get_len_width(max_w + 1)
      if w > self.width:
        self.width = w
    self.width += self.selector_dx
    self.height = self.fp.get_lines_height(model.item_count)
    self.arrow_left = self.graphics.load_image('data/img/arrow_left.png')
    self.arrow_right = self.graphics.load_image('data/img/arrow_right.png')

  def render(self):
    y = self.y
    control_x = self.x + self.control_x + self.fp.char_width
    for i in range(self.model.item_count):
      item = self.model.get_item(i)
      is_active = i == self.model.selected_item
      if is_active:
        self.graphics.set_font('green_light')
      else:
        self.graphics.set_font('green_dark')
      self.graphics.draw_text(item.text, self.x, y)
      self.render_control(item, control_x, y, is_active)
      if is_active:
        self.graphics.draw_image(self.selector, self.x + self.selector_dx, y)
      y += self.graphics.font_params.char_height + 10

  def render_control(self, item, x, y, is_selected):
    if item.type == MenuItem.TYPE_SLIDER:
      self.graphics.draw_rect(x, y + 6, 108, 32, (91,128,0))
      self.graphics.draw_rect(x + 4, y + 10, 100 * item.value, 24, (128,180,0))
      if is_selected:
        self.graphics.draw_image(self.arrow_left, x - 25, y + 14)
        self.graphics.draw_image(self.arrow_right, x + 114, y + 14)
    elif item.type == MenuItem.TYPE_LIST:
      str = item.value[item.position]
      str_width = self.fp.get_str_width(str)
      self.graphics.draw_text(str, x, y)
      if is_selected:
        self.graphics.draw_image(self.arrow_left, x - 25, y + 14)
        self.graphics.draw_image(self.arrow_right, x + 6 + str_width, y + 14)
