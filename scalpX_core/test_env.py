import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print("Discord Webhook URL:", os.getenv('DISCORD_WEBHOOK_URL'))
print("Google Sheets ID:", os.getenv('GOOGLE_SHEET_ID'))
print("Google Credentials File:", os.getenv('GOOGLE_CREDENTIALS_FILE'))
