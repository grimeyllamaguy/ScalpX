import discord
from discord.ext import tasks, commands
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

CHANNEL_IDS = {
    "live_trades": 123456789012345678,     # Replace with your real channel IDs
    "wins_losses": 123456789012345679,
    "progress_updates": 123456789012345680,
    "marketing": 123456789012345681,
}

class ScalpXBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_summary.start()
        logging.info("ScalpX Discord Bot initialized.")

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Logged in as {self.bot.user} (ID: {self.bot.user.id})")
        print(f"Logged in as {self.bot.user} (ID: {self.bot.user.id})")

    async def send_live_trade(self, trade_info):
        channel = self.bot.get_channel(CHANNEL_IDS['live_trades'])
        if channel:
            embed = discord.Embed(
                title="🚀 Live Trade Executed!",
                description=f"**{trade_info['ticker']}** at ${trade_info['entry']} entry, exited at ${trade_info['exit']} for {trade_info['pct_gain']} gain",
                color=0x1ABC9C
            )
            embed.set_footer(text="Powered by ScalpX")
            await channel.send(embed=embed)

    async def send_win_loss_update(self, result_info):
        channel = self.bot.get_channel(CHANNEL_IDS['wins_losses'])
        if channel:
            color = 0x2ECC71 if result_info['won'] else 0xE74C3C
            embed = discord.Embed(
                title="📈 Trade Result",
                description=f"Trade on **{result_info['ticker']}** resulted in a {'WIN' if result_info['won'] else 'LOSS'}.\n"
                            f"Gain/Loss: {result_info['pct_gain']}\nNotes: {result_info.get('notes', 'N/A')}",
                color=color
            )
            await channel.send(embed=embed)

    async def send_progress_update(self, message):
        channel = self.bot.get_channel(CHANNEL_IDS['progress_updates'])
        if channel:
            embed = discord.Embed(
                title="📊 ScalpX Progress Update",
                description=message,
                color=0x3498DB
            )
            await channel.send(embed=embed)

    async def send_marketing_blast(self, message):
        channel = self.bot.get_channel(CHANNEL_IDS['marketing'])
        if channel:
            embed = discord.Embed(
                title="🔥 ScalpX Marketing Blast",
                description=message,
                color=0xE67E22
            )
            await channel.send(embed=embed)

    @tasks.loop(hours=24)
    async def daily_summary(self):
        summary_channel = self.bot.get_channel(CHANNEL_IDS['progress_updates'])
        if summary_channel:
            await summary_channel.send("📅 Daily ScalpX Summary:\nTrades today: X\nWin rate: Y%\nProfit: $Z")

def start_bot(token):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Bot connected as {bot.user} (ID: {bot.user.id})")

    # This is important: add_cog is an async coroutine, so await it properly
    async def setup():
        await bot.add_cog(ScalpXBot(bot))

    async def runner():
        await setup()
        await bot.start(token)

    asyncio.run(runner())
