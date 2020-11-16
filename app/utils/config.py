import configparser

class Config:
  def __init__(self, filename):
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

  def get_section(self, section_name):
    section = getattr(self, section_name)
    return section