import re

def read_template(pth):
  print('Hello, good day!\nI want you to build me a video game by entering whatever you like based on the describtions in between the curly brackets.\n**************************************************************************************************************************')
  try:
    with open(pth) as f:
      script = f.read()
  except FileNotFoundError:
    print('The file path provided is not correct.')

  return script

def parse_template(text):
  string = 'It was a {Adjective} and {Adjective} {Noun}.'
  parts = tuple(map(lambda itm : itm.strip('{}'),re.findall(r'{\w+}', string)))
  stripped = re.sub(r'{\w+}','{}',string )
  return (stripped, parts)
  

def merge():
  pass

if __name__ == "__main__":
  read_template('assets/dark_and_stormy_night_template.txt')
  parse_template('It was a {Adjective} and {Adjective} {Noun}.')