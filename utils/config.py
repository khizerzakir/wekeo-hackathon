from configparser import ConfigParser

def load_config(filename='config.ini', section='database'):
  parser = ConfigParser()
  parser.read(filename)

  config = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      config[param[0]] = param[1]
  else:
    raise Exception('Section {0} was not found in the {1} file'.format(section, filename))
  
  return config

def load_db_config(filename='config.ini'):
  return load_config(filename, 'database')