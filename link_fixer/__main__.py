"""os module for .env file"""
import os
from dotenv import load_dotenv
from link_fixer import bot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot_runner = bot.CustomBot(command_prefix="!")
bot_runner.run(TOKEN)
