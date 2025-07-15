# ==== scalpx_risk_engine.py ====
# Calculates position size and stop loss level based on account risk and strategy rules

def calculate_position_size(account_balance, risk_percent, entry_price, stop_loss_price):
    """
    Calculates the number of shares to buy based on the user's risk settings.
    
    :param account_balance: Total capital available.
    :param risk_percent: Percentage of capital to risk (e.g. 2).
    :param entry_price: Price of entry.
    :param stop_loss_price: Price to exit if trade goes wrong.
    :return: Position size in shares (rounded).
    """
    risk_amount = account_balance * (risk_percent / 100)
    stop_loss_amount = abs(entry_price - stop_loss_price)

    if stop_loss_amount == 0:
        return 0  # Prevent division by zero
    
    position_size = risk_amount / stop_loss_amount
    return round(position_size)

def calculate_stop_loss(entry_price, risk_ratio=0.02):
    """
    Calculates a basic stop loss price based on risk ratio (2% default).
    :param entry_price: Price of entry
    :param risk_ratio: Stop loss percentage from entry
    :return: Stop loss price
    """
    return round(entry_price * (1 - risk_ratio), 2)

def calculate_take_profit(entry_price, reward_ratio=0.04):
    """
    Calculates take profit based on a reward ratio (e.g. 4% default).
    :param entry_price: Price of entry
    :param reward_ratio: Profit target percentage from entry
    :return: Take profit price
    """
    return round(entry_price * (1 + reward_ratio), 2)

# === Example usage ===
if __name__ == "__main__":
    balance = 1000
    risk_pct = 2
    entry = 150.00
    stop = calculate_stop_loss(entry)
    target = calculate_take_profit(entry)
    shares = calculate_position_size(balance, risk_pct, entry, stop)

    print(f"Entry: ${entry} | Stop: ${stop} | Target: ${target} | Shares: {shares}")
