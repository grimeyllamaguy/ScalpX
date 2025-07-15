# ==== scalpx_bot.py ====
import time
import yfinance as yf
import pandas as pd
from datetime import datetime

from scalpx_config import (
    LIVE_MODE, MIN_SCORE, WATCHLIST,
    DISCORD_WEBHOOK, EMAIL_SENDER, EMAIL_PASSWORD,
    EMAIL_RECEIVER, SMS_NUMBER
)

from scalpx_email_sms_discord import send_alert
from scalpx_risk_engine import calculate_position_size, calculate_stop_loss
from scalpx_trade_logger import log_trade
from scalpx_strategy_core import evaluate_trade

print("🔁 Starting ScalpX Bot...")
print(f"🎯 Mode: {'LIVE' if LIVE_MODE else 'PAPER'}")

while True:
    for ticker in WATCHLIST:
        try:
            df = yf.download(tickers=ticker, period="2d", interval="1m", progress=False)
            if df.empty or len(df) < 2:
                print(f"❌ No data for {ticker}")
                continue

            score = evaluate_trade(df)

            print(f"📊 {ticker} | Score: {score}")
            if score >= MIN_SCORE:
                entry_price = df['Close'].iloc[-1]
                stop_loss = calculate_stop_loss(entry_price)
                position = calculate_position_size(1000, 2, entry_price, stop_loss)

                alert_msg = (
                    f"🚨 Trade Signal Detected\n"
                    f"📈 Ticker: {ticker}\n"
                    f"🔢 Score: {score:.2f} (Min: {MIN_SCORE})\n"
                    f"💰 Entry: ${entry_price:.2f} | Stop: ${stop_loss:.2f} | Shares: {position}\n"
                    f"🧠 Strategy: AI Signal + Risk Filter"
                )

                send_alert(alert_msg)
                log_trade(
                    ticker=ticker,
                    signal_score=score,
                    entry_price=entry_price,
                    exit_price=entry_price * 1.02,
                    profit_loss=entry_price * 0.02 * position,
                    strategy="AI Signal",
                    notes="Auto-trade execution" if LIVE_MODE else "Paper mode log"
                )
        except Exception as e:
            print(f"⚠️ Error with {ticker}: {e}")

    time.sleep(15 if LIVE_MODE else 30)
