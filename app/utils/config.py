import configparser

class Config:
  def __init__(self, filename):
    self.config = None
    self.filename = filename
    self.read(filename)

  def read(self, filename):
    config = configparser.ConfigParser()
    config.read(filename)

    for section_name in config:
      section = config[section_name]
      if len(section) == 0:
        continue
      section_object = type('', (), {})
      for key in section:
        setattr(section_object, key, section[key])
      setattr(self, section_name, section_object)

    self.config = config

  def get_section(self, section_name):
    section = getattr(self, section_name)
    return section

  def save(self):
    self.config.set('window', 'width', str(self.window.width))
    self.config.set('window', 'height', str(self.window.height))
    self.config.set('window', 'fullscreen', 'yes' if self.window.fullscreen else 'no')
    self.config.set('game', 'sfx_volume', str(self.game.sfx_volume))
    self.config.set('game', 'music_volume', str(self.game.music_volume))
    fp = open(self.filename, 'w')
    self.config.write(fp)
    fp.close()