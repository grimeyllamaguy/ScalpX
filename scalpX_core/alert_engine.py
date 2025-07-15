import json
from integrations.discord_alert import send_discord_alert
from integrations.sms_alert import send_sms_alert
from integrations.gmail_alert import send_gmail_alert
from google_sheets_api import log_trade_to_sheet  # Assuming this function exists for Google Sheets

def handle_alert_data(data):
    # Extract necessary information from the webhook data
    symbol = data['symbol']
    price = data['price']
    signal = data['signal']
    
    # Log the alert data to Google Sheets
    log_trade_to_sheet(symbol, price, signal)

    # Send alerts to Discord
    send_discord_alert(symbol, price, signal)

    # Send SMS alert
    send_sms_alert(symbol, price, signal)

    # Send email alert
    send_gmail_alert(symbol, price, signal)
