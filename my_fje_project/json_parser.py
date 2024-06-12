import json

class Jsonparser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_json_data()
    def load_json_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_data(self):
        return self.data


