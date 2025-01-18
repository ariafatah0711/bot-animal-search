import pandas as pd

class DataLoader:
    def __init__(self, file_name, row_list, sheet = 'Sheet1'):
        self.file = file_name
        self.row = row_list
        self.sheet = sheet
    
    def load_data(self, sort=False):
        try:
            df = pd.read_excel(self.file, sheet_name=self.sheet, usecols=self.row)

            for row in self.row:
                df[row].fillna(method='ffill', inplace=True)
                        
        except ValueError:
            raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")

        if sort == True:
            df = df.sort_values(self.row[2]).reset_index(drop=True)

        return df