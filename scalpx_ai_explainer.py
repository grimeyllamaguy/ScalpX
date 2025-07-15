# ==== scalpx_ai_explainer.py ====
# Generates plain-English explanations for trades using GPT-style logic

def generate_trade_explanation(ticker, score, entry_price, exit_price, strategy, rsi=None, vwap=None):
    """
    Creates a human-readable explanation for why a trade was triggered.

    :param ticker: Stock ticker
    :param score: Strategy score used to justify trade
    :param entry_price: Price entered
    :param exit_price: Target or exit price
    :param strategy: Name of the strategy used
    :param rsi: Optional RSI value
    :param vwap: Optional VWAP value
    :return: String summary
    """
    result = "✅" if exit_price > entry_price else "❌"

    summary = (
        f"{result} Trade summary for {ticker}:\n"
        f"• Strategy used: {strategy}\n"
        f"• Entry at ${entry_price}, exit at ${exit_price} → Net {'gain' if result == '✅' else 'loss'} of ${round(abs(exit_price - entry_price), 2)}\n"
        f"• Signal Score: {score}/10"
    )

    if rsi is not None:
        summary += f"\n• RSI at time of entry: {rsi}"
    if vwap is not None:
        summary += f"\n• Price was {'above' if entry_price > vwap else 'below'} VWAP: ${vwap}"

    summary += f"\n• Reason: Signal score met threshold and matched trade criteria."

    return summary

# === Example Usage ===
if __name__ == "__main__":
    print(generate_trade_explanation("AAPL", 9.1, 173.50, 176.40, "VWAP Bounce", rsi=28, vwap=172.9))
