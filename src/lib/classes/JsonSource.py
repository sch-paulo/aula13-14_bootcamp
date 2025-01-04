import os
import json
from lib.classes.FilesSources import FilesSources

class JsonSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'json_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.json')]

        if new_files: 
            print(f'New JSON files detected: {new_files}')
            self.previous_files = current_files
        else:
            print('No new JSON files detected')
            self.get_data()

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f'Error while accessing JSON file: {e}')
            return None
        
    def get_data(self):
        data = []
        for file_path in self.previous_files:
            if file_path.endswith('.json'):
                path = os.path.join(self.folder_path, file_path)
                json_data = self.read_json_file(path)
                if json_data is not None:
                    data.append(json_data)
        print(data)
        return data