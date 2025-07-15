# 26/45: integrations/tradingview_webhook_handler.py
from flask import Flask, request, jsonify
from scalpX_core.alert_engine import handle_alert_data

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"[TRADINGVIEW ALERT RECEIVED]: {data}")
    handle_alert_data(data)  # Pass the alert data to your core logic
    return jsonify({"status": "Webhook received ✅"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
