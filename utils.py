import os

def get_first_json_file():
  files = os.listdir()
  return find_first_json(files)

def find_first_json(files):
  for file in files:
    if file.endswith('.json'):
      return file
  return None

