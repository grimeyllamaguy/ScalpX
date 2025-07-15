# ==== scalpx_trade_logger.py ====

import csv
import os
from datetime import datetime

LOG_FILE = "scalpx_trades_log.csv"

def log_trade(ticker, signal_score, entry_price, exit_price, profit_loss, strategy, notes):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp", "Ticker", "Signal Score", "Entry Price",
                "Exit Price", "P/L", "Strategy", "Notes"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ticker, signal_score, entry_price,
            exit_price, profit_loss, strategy, notes
        ])

    print(f"📝 Trade logged: {ticker} | P/L: ${profit_loss}")
