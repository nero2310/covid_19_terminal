import os.path

import pandas as pd


class PandasDataAnalyzer:
    def __init__(self, data):
        index_key = data[0].pop("lastChange")
        self.data_frame = pd.DataFrame(data, index=[index_key])

    def save_to_json(self, file_name="database.json"):
        if not os.path.isfile(file_name):
            try:
                self.data_frame.to_json(path_or_buf=file_name)
            except:
                pass

    def load_from_json(self):
        pass

    def print_data_frame(self):
        print(self.data_frame)