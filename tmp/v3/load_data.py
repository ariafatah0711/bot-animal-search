import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# class DataLoader:
#     def __init__(self, file_name, row_list, sheet = 'Sheet1'):
#         self.file = file_name
#         self.row = row_list
#         self.sheet = sheet
    
#     def load_data(self, sort=False):
#         try:
#             df = pd.read_excel(self.file, sheet_name=self.sheet, usecols=self.row)

#             for row in self.row:
#                 df[row].fillna(method='ffill', inplace=True)
                        
#         except ValueError:
#             raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")

#         if sort == True:
#             df = df.sort_values(self.row[2]).reset_index(drop=True)

#         return df

# class DataLoader:
#     def __init__(self, spreadsheet_id, row_list, sheet='Sheet1', credentials='credentials.json'):
#         self.spreadsheet_id = spreadsheet_id
#         self.row = row_list
#         self.sheet = sheet
#         self.credentials = credentials

#     def _authorize_google_sheets(self):
#         # Setup scope untuk Google Sheets API
#         scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#         creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials, scope)
#         client = gspread.authorize(creds)
#         return client

#     def load_data(self, sort=False):
#         try:
#             client = self._authorize_google_sheets()
#             # Buka spreadsheet berdasarkan ID
#             spreadsheet = client.open_by_key(self.spreadsheet_id)
#             worksheet = spreadsheet.worksheet(self.sheet)

#             # Baca data menjadi DataFrame
#             data = worksheet.get_all_records()
#             df = pd.DataFrame(data)[self.row]

#             # Isi nilai kosong (jika ada)
#             for row in self.row:
#                 df[row].fillna(method='ffill', inplace=True)

#         except gspread.exceptions.SpreadsheetNotFound:
#             raise ValueError(f"Spreadsheet dengan ID '{self.spreadsheet_id}' tidak ditemukan.")
#         except gspread.exceptions.WorksheetNotFound:
#             raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")

#         if sort:
#             df = df.sort_values(self.row[2]).reset_index(drop=True)

#         return df


# class DataLoader:
#     def __init__(self, spreadsheet_id, row_list, sheet='Sheet1', credentials='credentials.json'):
#         self.spreadsheet_id = spreadsheet_id
#         self.row = row_list
#         self.sheet = sheet
#         self.credentials = credentials

#     def _authorize_google_sheets(self):
#         scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#         creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials, scope)
#         client = gspread.authorize(creds)
#         return client

#     def load_data(self, sort=False):
#         try:
#             client = self._authorize_google_sheets()
#             spreadsheet = client.open_by_key(self.spreadsheet_id)
#             worksheet = spreadsheet.worksheet(self.sheet)

#             # Baca data menjadi DataFrame
#             data = worksheet.get_all_records()
#             df = pd.DataFrame(data) 

#             # Filter kolom yang diperlukan
#             df = df[self.row]

#             # Isi nilai kosong
#             for row in self.row:
#                 df[row].fillna(method='ffill', inplace=True)

#             if sort:
#                 df = df.sort_values(by=df.columns[2]).reset_index(drop=True)

#             return df

#         except gspread.exceptions.SpreadsheetNotFound:
#             raise ValueError(f"Spreadsheet dengan ID '{self.spreadsheet_id}' tidak ditemukan.")
#         except gspread.exceptions.WorksheetNotFound:
#             raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")import pandas as pd


class DataLoader:
    def __init__(self, spreadsheet_id, row_list, sheet='Sheet1', credentials='credentials.json'):
        self.spreadsheet_id = spreadsheet_id
        self.row = row_list
        self.sheet = sheet
        self.credentials = credentials

    def _authorize_google_sheets(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials, scope)
        client = gspread.authorize(creds)
        return client

    def load_data(self, sort=False):
        try:
            client = self._authorize_google_sheets()
            spreadsheet = client.open_by_key(self.spreadsheet_id)
            worksheet = spreadsheet.worksheet(self.sheet)

            # Baca data menjadi DataFrame
            data = worksheet.get_all_records()
            if not data:
                raise ValueError("Data di Google Sheets kosong atau tidak ditemukan.")

            df = pd.DataFrame(data)

            # Debug: Cetak nama kolom yang tersedia
            print("Kolom yang tersedia:", df.columns.tolist())

            # Filter kolom yang diperlukan (cek apakah kolom ada)
            missing_columns = [col for col in self.row if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Kolom berikut tidak ditemukan di DataFrame: {missing_columns}")

            df = df[self.row]

            # Isi nilai kosong
            for row in self.row:
                df[row].fillna(method='ffill', inplace=True)

            # Sort data jika diperlukan
            if sort:
                df = df.sort_values(by=self.row[2]).reset_index(drop=True)

            return df

        except gspread.exceptions.SpreadsheetNotFound:
            raise ValueError(f"Spreadsheet dengan ID '{self.spreadsheet_id}' tidak ditemukan.")
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"Sheet dengan nama '{self.sheet}' tidak ditemukan.")