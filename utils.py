import os

def get_most_recent_json_file():
    json_files = get_all_json_files()
    if len(json_files) == 0:
        return None

    most_recent_time = 0
    recent_file = ''
    for file in json_files:
       _, _, _, _, _, _, _, _, modification_at, _ = os.stat(file)
       if modification_at > most_recent_time:
           most_recent_time = modification_at
           recent_file = file

    if recent_file == '':
        return None

    return recent_file

def get_all_json_files():
    files = os.listdir()
    json_files = []
    for file in files:
        if file.endswith('.json'):
            json_files.append(file)
    return json_files

def get_first_json_file():
    json_files = get_all_json_files()
    if len(json_files) == 0:
        return None
    return json_files[0]

