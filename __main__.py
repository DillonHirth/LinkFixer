"""os module for .env file"""
import os
from dotenv import load_dotenv
from bot_src.bot import CustomBot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = CustomBot(command_prefix="!")
bot.run(TOKEN)
