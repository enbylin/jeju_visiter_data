from oauth2client.service_account import ServiceAccountCredentials
import gspread
from api import google_key

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(google_key, scope)

sheet_name = "api_test"
client = gspread.authorize(creds)
sps = client.open(sheet_name)

tab1_sheet = sps.worksheet("tab1")

print(tab1_sheet.get_all_values())

    