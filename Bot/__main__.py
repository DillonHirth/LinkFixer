import os
from bot import CustomBot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = CustomBot(command_prefix="!")
bot.run(TOKEN)
#test
