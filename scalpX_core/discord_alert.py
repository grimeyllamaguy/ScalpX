import requests

def send_discord_alert(symbol, price, signal):
    webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
    message = {
        "content": f"Trade Signal Alert!\nSymbol: {symbol}\nPrice: ${price}\nSignal: {signal}"
    }

    response = requests.post(webhook_url, json=message)
    if response.status_code == 200:
        print(f"Discord alert sent successfully for {symbol}")
    else:
        print(f"Failed to send Discord alert for {symbol}")
