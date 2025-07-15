# ==== scalpx_dashboard.py ====
import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

st.set_page_config(page_title="ScalpX Live Dashboard", layout="wide")

# Load trade log
TRADE_LOG_FILE = "scalpx_trades.csv"

def load_trades():
    if os.path.exists(TRADE_LOG_FILE):
        return pd.read_csv(TRADE_LOG_FILE)
    else:
        return pd.DataFrame(columns=["Timestamp", "Ticker", "Signal Score", "Entry Price", "Exit Price", "P/L", "Strategy", "Notes"])

# Sidebar
st.sidebar.title("⚙️ ScalpX Controls")
refresh_rate = st.sidebar.slider("Refresh every X seconds", 5, 60, 15)

st.title("📊 ScalpX Live Trade Dashboard")
st.markdown("Real-time tracking of AI-driven scalp trades")

df = load_trades()

if df.empty:
    st.warning("No trades logged yet.")
else:
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df.sort_values("Timestamp", ascending=False)
    
    # KPIs
    total_trades = len(df)
    total_profit = df["P/L"].sum()
    win_rate = (df["P/L"] > 0).sum() / total_trades * 100 if total_trades > 0 else 0
    avg_profit = df["P/L"].mean() if total_trades > 0 else 0

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Trades", total_trades)
    kpi2.metric("Total P/L ($)", round(total_profit, 2))
    kpi3.metric("Win Rate (%)", f"{win_rate:.2f}")
    kpi4.metric("Avg P/L ($)", round(avg_profit, 2))

    # Recent trades
    st.subheader("📈 Trade History")
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)

    # Chart
    st.subheader("📉 P/L Over Time")
    profit_chart = df.copy()
    profit_chart["Running P/L"] = profit_chart["P/L"].cumsum()
    st.line_chart(profit_chart.set_index("Timestamp")["Running P/L"])

# Auto-refresh
st.experimental_rerun()
