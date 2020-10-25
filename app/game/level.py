class Level:
  NONE = 0
  FIELD = 1
  WALL = 10
  HEAD = 20
  TAIL = 30
  APPLE = 40

  def __init__(self, lines):
    self.start_addr = 0
    self.line_length = 0
    self.data = None
    self.free_cells = 0
    self.build(lines)

  def build(self, lines):
    self.line_length = 0
    for line in lines:
      l = len(line)
      if l > self.line_length:
        self.line_length = l

    level = bytearray(len(lines) * self.line_length)

    line_addr = 0
    for line in lines:
      offset = line_addr
      for char in line:
        if char == '.':
          level[offset] = self.FIELD
          self.free_cells += 1
        elif char == '#':
          level[offset] = self.WALL
        elif char == '@':
          level[offset] = 1
          self.start_addr = offset
        offset += 1
      line_addr += self.line_length

    self.data = level
