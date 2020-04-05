import gspread
from oauth2client.service_account import ServiceAccountCredentials
import states


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1XIP7hWgGL_aEfRBHyFqiRGwGGrqLCejfCkHgvRNjC7A/edit#gid=0').sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
sheet.update_acell('D1', 'Witam!')
sheet.update_cell(5, 5, 'Żegnam!')


