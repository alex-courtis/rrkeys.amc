import os

def get_first_json_file():
  files = os.listdir()
  json_file = next((file for file in files if file.endswith('.json')), None)
  return json_file