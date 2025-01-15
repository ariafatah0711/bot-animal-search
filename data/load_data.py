import pandas as pd

# def load_data(file, row):
#     if (not file):
#         file = "data_example.xlsx"
#     if (not row):
#         row = ["pattern", "value", "priority"]    
    
#     # df = pd.read_excel(file, usecols=row) # default
#     df = pd.read_excel(file, usecols=row).sort_values(row[2]).reset_index(drop=True) # sort value by priority and reset index
#     return df

class DataLoader:
    def __init__(self, file_name, row_list, sheet = 'Sheet1'):
        self.file = file_name
        self.row = row_list
        self.sheet = sheet
    
    def load_data(self, sort=False):
        try:
            df = pd.read_excel(self.file, sheet_name=self.sheet, usecols=self.row)
        except ValueError:
            raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")

        if sort == True:
            df = df.sort_values(self.row[2]).reset_index(drop=True)

        return df