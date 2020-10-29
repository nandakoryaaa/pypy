class Level:
  NONE = 0
  FIELD = 1
  WALL = 10
  HEAD = 20
  TAIL = 30
  APPLE = 40

  def __init__(self, lines):
    self.start_addr = 0
    self.width = 0
    self.height = 0
    self.data = None
    self.free_cells = 0
    self.build(lines)

  def build(self, lines):
    self.width = 0
    self.height = len(lines)
    for line in lines:
      line = line.rstrip()
      l = len(line)
      if l > self.width:
        self.width = l

    level = bytearray(len(lines) * self.width)

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
      line_addr += self.width

    self.data = level
