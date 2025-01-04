import os
import pandas as pd
from lib.classes.FilesSources import FilesSources

class CsvSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'csv_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.csv')]

        if new_files:
            print(f'New CSV files detected: {new_files}')
            self.previous_files = current_files
        else:
            print('No new CSV files detected')
            self.get_data()
        
    def get_data(self):
        # Implement getting data from CSV files in the specified folder
        dataframes = []
        for file_path in self.previous_files:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pd.read_csv(path)
                dataframes.append(data)
            except Exception as e:
                print(f'An error occurred while reading the CSV file: {e}')
        if dataframes:
            self.combined_data = pd.concat(dataframes, ignore_index=True)
            print(self.combined_data)
            return self.combined_data
        else:
            return None


    def transform_data_to_df(self):
        return super().transform_data_to_df()

    def save_data(self):
        pass

    def show_files(self):
        print(self.previous_files)
    
    def start(self):
        self.create_path()