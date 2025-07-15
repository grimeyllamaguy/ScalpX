# ==== scalpx_email_sms_discord.py ====

import smtplib
from email.message import EmailMessage
import requests

from scalpx_config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, DISCORD_WEBHOOK

def send_email(subject, content):
    try:
        email = EmailMessage()
        email["From"] = EMAIL_SENDER
        email["To"] = EMAIL_RECEIVER
        email["Subject"] = subject
        email.set_content(content)

        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(email)
        smtp.quit()
        print("📧 Email sent!")
    except Exception as e:
        print(f"❌ Email send failed: {e}")

def send_discord(content):
    try:
        data = {"content": content}
        response = requests.post(DISCORD_WEBHOOK, json=data)
        if response.status_code == 204:
            print("✅ Discord alert sent!")
        else:
            print(f"❌ Discord failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Discord error: {e}")

def send_sms(content):
    # Placeholder: You’d use Twilio API or another service here
    print(f"📱 SMS: {content} (simulation)")

def send_alert(content):
    send_email("🚨 ScalpX Trade Alert", content)
    send_discord(content)
    send_sms(content)
