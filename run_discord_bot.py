import os
from discord_bot import start_bot
from dotenv import load_dotenv

load_dotenv()  # loads .env file

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not DISCORD_BOT_TOKEN or DISCORD_BOT_TOKEN.strip() == "":
    print("❌ ERROR: DISCORD_BOT_TOKEN missing or empty in .env")
    exit(1)

start_bot(DISCORD_BOT_TOKEN)
