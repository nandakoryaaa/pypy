class MainMenuModel:
  def __init__(self, loader, item_list):
    self.loader = loader
    self.img_selector = loader.load_image('data/graphics/menu_select.png')
    self.selected_item = 0
    self.load(item_list)

  def load(self, item_list):
    self.item_count = len(item_list)
    self.menu = []
    self.width = 0
    for img_name in item_list:
      img = self.loader.load_image('data/graphics/menu_' + img_name + '.png')
      img_hi = self.loader.load_image('data/graphics/menu_' + img_name + '_hi.png')
      self.menu.append((img, img_hi))
      w = img.get_width()
      if (w > self.width):
        self.width = w
    self.item_height = self.menu[0][0].get_height() + 10

  def next_item(self):
    self.selected_item += 1
    if self.selected_item == self.item_count:
      self.selected_item = 0

  def prev_item(self):
    self.selected_item -= 1
    if self.selected_item < 0:
      self.selected_item = self.item_count - 1

  def get_item(self, num):
    if (num == self.selected_item):
      return self.menu[num][1]
    return self.menu[num][0]

  def get_selector(self):
    return self.img_selector
