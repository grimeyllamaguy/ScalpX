# ==== scalpx_webhook_listener.py ====
from flask import Flask, request, jsonify
import threading
from scalpx_trade_logger import log_trade
from scalpx_email_sms_discord import send_alert
from scalpx_config import WATCHLIST, MIN_SCORE

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if not data or 'ticker' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    ticker = data['ticker']
    score = float(data['score'])

    if ticker not in WATCHLIST:
        return jsonify({'error': 'Ticker not in watchlist'}), 403

    if score >= MIN_SCORE:
        msg = f"🚨 Webhook Signal Received: {ticker} scored {score}"
        send_alert(msg)

        log_trade(
            ticker=ticker,
            signal_score=score,
            entry_price=data.get("entry_price", 0),
            exit_price=data.get("exit_price", 0),
            profit_loss=data.get("profit_loss", 0),
            strategy=data.get("strategy", "Webhook Trigger"),
            notes=data.get("notes", "Triggered via webhook")
        )

        return jsonify({'status': 'Alert handled'}), 200

    return jsonify({'status': 'Score below threshold'}), 202

def run_server():
    app.run(host='0.0.0.0', port=5001)

if __name__ == "__main__":
    print("🔌 Starting ScalpX Webhook Listener on port 5001...")
    threading.Thread(target=run_server).start()
