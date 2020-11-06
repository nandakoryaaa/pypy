from app.models.menuitem import MenuItem

class MenuModel:
  def __init__(self, loader, item_list):
    self.loader = loader
    self.item_list = item_list
    self.item_count = len(item_list)
    self.selected_item = 0
    self.width = 0
    self.height = 0
    for item in item_list:
      item.img = self.loader.load_image('data/img/' + item.file + '.png')
      item.img_hi = self.loader.load_image('data/img/' + item.file + '_hi.png')
      w = item.img.get_width()
      if w > self.width:
        self.width = w
      self.height += item.img.get_height()
    self.img_selector = loader.load_image('data/img/menu_select.png')

  def next_item(self):
    self.selected_item += 1
    if self.selected_item == self.item_count:
      self.selected_item = 0

  def prev_item(self):
    self.selected_item -= 1
    if self.selected_item < 0:
      self.selected_item = self.item_count - 1

  def get_item(self, num):
    return self.item_list[num]

  def get_selected_item(self):
    return self.item_list[self.selected_item]

  def get_selector(self):
    return self.img_selector
