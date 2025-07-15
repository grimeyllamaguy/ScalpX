# ==== scalpx_strategy_core.py ====
# Generates a strategy score based on technical confluence: VWAP, RSI, Candles

import pandas as pd

def evaluate_trade(df):
    """
    Evaluates a trading opportunity using technical confluence:
    VWAP proximity, RSI conditions, and candlestick formation.

    :param df: DataFrame with 'Close', 'VWAP', 'RSI', 'Open', 'High', 'Low'
    :return: float - signal score out of 10
    """
    if df.empty or 'Close' not in df.columns:
        return 0.0

    latest = df.iloc[-1]

    # === VWAP Confluence ===
    vwap_diff = abs(latest['Close'] - latest['VWAP'])
    vwap_score = max(0, 3 - (vwap_diff / latest['VWAP']) * 100)

    # === RSI Behavior ===
    if latest['RSI'] < 30:
        rsi_score = 2.5  # Oversold bounce potential
    elif latest['RSI'] > 70:
        rsi_score = -1.5  # Overbought risk
    else:
        rsi_score = 1.0  # Neutral range strength

    # === Candlestick Strength ===
    candle_score = 0
    if latest['Close'] > latest['Open']:
        candle_score += 1.5  # Bullish body
    if latest['Close'] > latest['High'] - 0.2 * (latest['High'] - latest['Low']):
        candle_score += 1.0  # Strong close near high

    # === Total Strategy Score ===
    total_score = round(vwap_score + rsi_score + candle_score, 2)
    return total_score
