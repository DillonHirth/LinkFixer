"""
os: to reference environment variables
dotenv: used to read key:value pairs from the .env file and loads them as env variables
    https://github.com/theskumar/python-dotenv
"""
import os
from dotenv import load_dotenv
from link_fixer import bot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot_runner = bot.CustomBot(command_prefix="!")
bot_runner.run(TOKEN)
