class Level:
  NONE = 0
  FIELD = 1
  WALL = 10
  HEAD = 20
  TAIL = 30
  APPLE = 40
  EXIT = 50

  def __init__(self, lines):
    self.apple_count = 0
    self.start_addr = 0
    self.growth = 0
    self.timer = 0
    self.apple_timer = 0
    self.width = 0
    self.height = 0
    self.data = None
    self.free_cells = 1
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
        elif char == 'E':
          level[offset] = self.EXIT
        offset += 1
      line_addr += self.width

    self.data = level

  def get_free_cells(self, buffer):
    buffer_pos = 0
    for i in range(self.width + 1, len(self.data) - self.width - 1):
      if self.data[i] == self.FIELD:
        buffer[buffer_pos] = i
        buffer_pos += 1
    return buffer_pos

    