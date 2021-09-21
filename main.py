import os
import random
import discord
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
EMAIL = os.getenv('IFUNNY_EMAIL')
PASS = os.getenv('IFUNNY_PW')
headers = {
    'user-agent': 'linkFixer/0.0.1',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def get_url_src(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        only_meta_tags = SoupStrainer("meta")
        print("request status_code:", res.status_code)
        soup = BeautifulSoup(res.content, 'html.parser', parse_only=only_meta_tags)

        for link in soup.find_all('meta'):
            if link.get('property') == "og:video:secure_url":
                direct_link = (link.get('content'))
                break
        return direct_link
    else:
        print("bad response:", res.status_code)


# get_url_src('https://ifunny.co')


class CustomBot(commands.Bot):

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(f'{guild.name} (id: {guild.id})\n')

    async def on_message(self, message):
        if message.author == bot.user:
            return
        if 'ifunny.co' in message.content:
            print("message content:", message.content)
            response = get_url_src(message.content)
            await message.channel.send(response)
        await self.process_commands(message)

bot = CustomBot(command_prefix="!")
bot.run(TOKEN)
