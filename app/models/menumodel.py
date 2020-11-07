from app.models.menuitem import MenuItem

class MenuModel:
  def __init__(self, loader, item_list):
    self.loader = loader
    self.item_list = item_list
    self.item_count = len(item_list)
    self.selected_item = 0

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
