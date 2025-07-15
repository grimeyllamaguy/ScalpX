# ==== scalpx_auto_xp.py ====
import json
import os

XP_FILE = "scalpx_xp.json"

def load_xp():
    if os.path.exists(XP_FILE):
        with open(XP_FILE, "r") as f:
            return json.load(f)
    return {"xp": 0, "trades": 0}

def save_xp(data):
    with open(XP_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_trade_xp(points=10):
    data = load_xp()
    data["xp"] += points
    data["trades"] += 1
    save_xp(data)
    print(f"🎯 XP Updated → {data['xp']} XP from {data['trades']} trades.")

if __name__ == "__main__":
    add_trade_xp()
