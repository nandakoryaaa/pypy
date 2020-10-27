from app.views.view import View

class MainMenuView(View):
  def __init__(self, graphics, model):
    super().__init__(graphics, model)
    self.img_logo = graphics.load_image('data/graphics/main_menu_title.png').convert()
    self.menu_x = (self.graphics.screen_width - self.model.width) // 2
    logo_height = self.img_logo.get_height()
    self.menu_y = logo_height + (self.graphics.screen_height - logo_height - self.model.item_height * self.model.item_count) // 2
    self.selector = self.model.get_selector()
    self.selector_x = self.menu_x - self.selector.get_width() - 15

  def render(self):
    self.graphics.fill((0,0,0))
    self.graphics.draw_image(self.img_logo, 0, 0)
    for i in range(self.model.item_count):
      y = self.menu_y + i * self.model.item_height
      item = self.model.get_item(i)
      self.graphics.draw_image(item, self.menu_x, y)
      if i == self.model.selected_item:
        self.graphics.draw_image(self.selector, self.selector_x, y)

