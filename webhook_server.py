from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Discord webhook URL from .env
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Function to send Discord alert
def send_discord_alert(symbol, price, signal):
    discord_message = {
        "content": f"Trade Alert: {signal} on {symbol} at ${price}"
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=discord_message)
        if response.status_code == 204:
            print("Discord alert sent successfully!")
        else:
            print(f"Failed to send Discord alert: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Discord alert: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Print out the webhook data for debugging purposes
        print("✅ Webhook received:")
        print(data)

        # Extract data from the incoming webhook
        ticker = data.get("ticker")
        price = data.get("price")
        signal = data.get("signal")
        confidence = data.get("confidence")
        timestamp = data.get("timestamp")

        # Print the formatted message to the console
        print(f"📈 {signal} signal on {ticker} at ${price} ({confidence}% confidence) at {timestamp}")

        # Send Discord alert
        send_discord_alert(ticker, price, signal)

        # Returning a success response back to the sender
        return jsonify({"status": "success", "message": "Webhook received"}), 200

    except Exception as e:
        # If there's an error, print it out and return an error message
        print(f"❌ Error in webhook handler: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on all network interfaces (0.0.0.0) and listen on port 5001
    app.run(host='0.0.0.0', port=5001, debug=True)
