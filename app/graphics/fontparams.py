class FontParams:
  def __init__(self, start_x, start_y, char_width, char_height, char_spacing, line_spacing, chars_in_line, map):
    self.start_x = start_x
    self.start_y = start_y
    self.char_width = char_width
    self.char_height = char_height
    self.char_spacing = char_spacing
    self.line_spacing = line_spacing
    self.chars_in_line = chars_in_line
    self.map = map

  def get_str_width(self, str):
    length = len(str)
    return self.get_len_width(length)

  def get_len_width(self, num):
    if num < 1:
      return 0
    return (self.char_width + self.char_spacing) * num - self.char_spacing

  def get_lines_height(self, num, spacing = None):
    if num < 1:
      return 0
    if spacing is None:
      spacing = self.line_spacing
    return (self.char_height + spacing) * num - spacing
    