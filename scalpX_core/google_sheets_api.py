import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets API
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("YOUR_CREDENTIALS_FILE.json", scope)
    client = gspread.authorize(creds)
    return client

def log_trade_to_sheet(symbol, price, signal):
    client = authenticate_google_sheets()
    sheet = client.open("YourGoogleSheetName").sheet1

    # Log trade data to the first row of the sheet
    row = [symbol, price, signal]
    sheet.append_row(row)
    print(f"Trade logged to Google Sheets: {symbol} at {price} with signal {signal}")
