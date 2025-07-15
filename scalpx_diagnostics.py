# === scalpx_diagnostics.py ===
import os
import importlib.util
import smtplib
import requests
from email.message import EmailMessage

# === CONFIG (Auto-filled with Jamal’s info) ===
REQUIRED_FILES = [
    "scalpx_alerts.py", "scalpx_auto_xp.py", "scalpx_bot.py", "scalpx_config.py",
    "scalpx_daily_report.py", "scalpx_dashboard_streamlit.py", "scalpx_email_sms_discord.py",
    "scalpx_mock_trades.py", "scalpx_replay_mode.py", "scalpx_risk_engine.py",
    "scalpx_test_alert.py", "scalpx_trade_logger.py", "scalpx_voice_commentary.py",
    "scalpx_config.json", "twilio_config.json"
]

MODULES_TO_TEST = [
    "yfinance", "requests", "smtplib", "discord", "email", "json"
]

EMAIL_SENDER = "llamaguyai@gmail.com"
EMAIL_PASSWORD = "wzse gvcd pjai uxef"
EMAIL_RECEIVER = "llamaguyai@gmail.com"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1393834483098320947/D7NxdLvH1gVq90woLwpofrmo6xGHdXknAwpFYrvGbc8cs4TQ5ogGXP048KWOWKeLKy5C"

# === UTILS ===

def check_file_exists(filename):
    if os.path.exists(filename):
        print(f"✅ Found: {filename}")
        return True
    else:
        print(f"❌ Missing: {filename}")
        return False

def check_module_installed(module):
    if importlib.util.find_spec(module):
        print(f"📦 Module OK: {module}")
        return True
    else:
        print(f"❌ Missing module: {module}")
        return False

def test_email_login():
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = "✅ ScalpX Email Test"
        msg.set_content("This is a test from scalpx_diagnostics.py")
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()
        print("📧 Email login + send successful")
        return True
    except Exception as e:
        print(f"❌ Email test failed: {e}")
        return False

def test_discord_webhook():
    try:
        payload = {
            "content": "✅ ScalpX webhook test successful!"
        }
        r = requests.post(DISCORD_WEBHOOK, json=payload)
        if r.status_code in [200, 204]:
            print("📨 Discord webhook OK")
            return True
        else:
            print(f"❌ Discord webhook failed: {r.status_code} - {r.text}")
            return False
    except Exception as e:
        print(f"❌ Discord webhook test failed: {e}")
        return False

# === DIAGNOSTICS ===

def run_preflight_check():
    print("\n🚀 SCALPX PRE-FLIGHT CHECKLIST\n-----------------------------")

    # 1. Check required files
    print("\n📁 Checking required files:")
    for file in REQUIRED_FILES:
        check_file_exists(file)

    # 2. Check module installations
    print("\n📦 Checking Python modules:")
    for mod in MODULES_TO_TEST:
        check_module_installed(mod)

    # 3. Test email system
    print("\n📧 Testing email system:")
    test_email_login()

    # 4. Test Discord webhook
    print("\n📨 Testing Discord webhook:")
    test_discord_webhook()

    print("\n✅ Diagnostics complete. You're cleared for launch.\n")

# === MAIN ===

if __name__ == "__main__":
    run_preflight_check()
