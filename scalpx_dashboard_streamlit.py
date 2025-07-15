# ==== scalpx_dashboard_streamlit.py ====
import streamlit as st
import json
import os

st.set_page_config(page_title="ScalpX Dashboard", layout="wide")

st.title("📊 ScalpX Trading Dashboard")

# XP Tracker
xp_data = {"xp": 0, "trades": 0}
if os.path.exists("scalpx_xp.json"):
    with open("scalpx_xp.json", "r") as f:
        xp_data = json.load(f)

st.metric("🔥 XP", xp_data["xp"])
st.metric("✅ Trades Logged", xp_data["trades"])

# Trade Log Display
st.subheader("📒 Recent Trades")
if os.path.exists("trade_log.json"):
    with open("trade_log.json", "r") as f:
        trades = json.load(f)
        for trade in trades[-10:][::-1]:
            st.json(trade)
else:
    st.write("No trades logged yet.")
