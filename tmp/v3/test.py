import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace the placeholders with your API credentials
creds = service_account.Credentials.from_service_account_file(
    'key.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
)

# Initialize the Google Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Replace the placeholders with your spreadsheet ID and range
spreadsheet_id = '1m7AZx05qk4KqHcg9q4esKG2AMXfJbmWIxM77PUNRT2k'
range_name = 'Sheet1!A1:D68'

# Fetch data from the Google Sheets
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])

# Convert the data into a DataFrame
if values:
    df = pd.DataFrame(values[1:], columns=values[0])  # Use the first row as header
    print(df.head())
else:
    print("No data found.")