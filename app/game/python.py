class Python:
  INIT = 0
  MOVE = 1
  GROW = 2
  SHRINK = 3
  DEAD = 4

  def __init__(self, start_addr, buffer_size):
    self.length = 1
    self.buffer_size = buffer_size
    self.count = 0
    self.mode = self.INIT
    self.dir = None
    self.body = [None] * buffer_size
    self.head = 0
    self.tail = 0
    self.body[self.head] = start_addr
    self.body[self.tail] = start_addr

  def set_dir(self, dir):
    if self.mode == self.DEAD or self.mode == self.SHRINK:
      return
    if (self.mode == self.INIT):
      self.mode = self.GROW
      self.count = 1
    self.dir = dir

  def update(self):
    if self.count == 0:
      return
    self.count -= 1
    if self.count > 0:
      return
    if self.mode == self.GROW:
      self.mode = self.MOVE
    elif self.mode == self.SHRINK:
      self.mode = self.DEAD

  def move_head(self, addr):
    if self.mode != self.MOVE and self.mode != self.GROW:
      return
    if self.head == 0:
      self.head = self.buffer_size
    self.head -= 1
    self.body[self.head] = addr
    self.length += 1

  def move_tail(self):
    if self.mode != self.MOVE and self.mode != self.SHRINK:
      return
    if self.tail == 0:
      self.tail = self.buffer_size
    self.tail -= 1
    self.length -= 1

  def set_mode(self, mode, count):
    if (self.mode != mode):
      self.count = 0
    self.count += count
    self.mode = mode

  def get_tail_addr(self):
    return self.body[self.tail]

  def get_head_addr(self):
    return self.body[self.head]

  def reset(self, start_addr):
    self.length = 1
    self.count = 0
    self.mode = self.INIT
    self.dir = None
    self.head = 0
    self.tail = 0
    self.body[self.head] = start_addr
    self.body[self.tail] = start_addr
