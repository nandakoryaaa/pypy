class MenuItem:
  PLAY = 0
  OPTIONS = 1
  HALL_OF_FAME = 2
  QUIT = 3
  MUSIC = 10
  SOUND = 11
  MAIN_MENU = 12
  CONTINUE = 13

  TYPE_NONE = 0
  TYPE_SLIDER = 1
  TYPE_SWITCH = 2

  def __init__(self, id, text, type = None, value = 0):
    self.id = id
    self.text = text
    self.type = type
    self.value = value
