class MenuItem:
  PLAY = 0
  SETUP = 1
  HALL_OF_FAME = 2
  QUIT = 3
  MUSIC = 10
  SOUND = 11
  MAIN_MENU = 12
  SCREEN_SIZE = 13
  FULLSCREEN = 14
  SAVE = 15
  CANCEL = 16
  CONTINUE = 17

  TYPE_NONE = 0
  TYPE_SLIDER = 1
  TYPE_LIST = 2

  def __init__(self, id, text, type = None, value = 0, position = 0):
    self.id = id
    self.text = text
    self.type = type
    self.value = value
    self.position = position

  def calc_value(self, step):
    self.value += step
    if self.value < 0:
      self.value = 0
    elif self.value > 1:
      self.value = 1
    return self.value
  
  def calc_position(self, step):
    length = len(self.value) - 1
    self.position += step
    if self.position < 0:
      self.position = length
    elif self.position > length:
      self.position = 0
    return self.position