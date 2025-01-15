import pandas as pd

def load_data():
    file = "data-animals.xlsx"
    row = ["pattern", "value", "priority"]
    # df = pd.read_excel(file, usecols=row) # default
    df = pd.read_excel(file, usecols=row).sort_values(row[2]).reset_index(drop=True) # sort value by priority and reset index
    return df