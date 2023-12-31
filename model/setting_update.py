import json

class SettingUpdater:
    def __init__(self, filepath):
        self.filepath = filepath

    def update_time_to_wait(self, new_time):
        with open(self.filepath, 'r+') as file:
            data = json.load(file)
            data['timeToWait'] = new_time
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def update_cursor_position(self, new_x, new_y):
        with open(self.filepath, 'r+') as file:
            data = json.load(file)
            data['cursorPosition']['x'] = new_x
            data['cursorPosition']['y'] = new_y
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def get_cursor_position(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            return data['cursorPosition']['x'], data['cursorPosition']['y']
    
    def get_time_to_wait(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            return data['timeToWait']


