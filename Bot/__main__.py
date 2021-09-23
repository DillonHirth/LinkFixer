import os
from bot import CustomBot

TOKEN = os.getenv('DISCORD_TOKEN')

bot = CustomBot(command_prefix="!")
bot.run(TOKEN)
