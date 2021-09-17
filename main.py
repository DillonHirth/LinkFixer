import json
import os
import random
import discord
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from discord.ext import commands
from requests.auth import HTTPBasicAuth

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
EMAIL = os.getenv('IFUNNY_EMAIL')
PASS = os.getenv('IFUNNY_PW')

headers = {
            'user-agent': 'linkFixer/0.0.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'TE': 'trailers'
}

import requests
response = requests.get("https://ifunny.co/video/HNtYjOTu8?s=cl", headers=headers)
print(response)


class CustomBot(commands.Bot):

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(f'{guild.name} (id: {guild.id})\n')

    async def on_message(self, message):
        if message.author == bot.user:
            return
        randomQuotes = [
            'Force, your very bad',
            'GetGud',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
                'but still, your trash'
            ),
            'Your choice'
        ]
        if message.content == 'forcekin':
            response = random.choice(randomQuotes)
            await message.channel.send(response)
        elif message.content == 'raise-exception':
            raise discord.DiscordException
        await self.process_commands(message)

        if 'ifunny.co' or '9gag.com' in message.content:
            def create_session(url):
                # create a Session
                s = requests.Session()
                # auth in
                res = s.get(message.content)
                if res.status_code == 200:
                    return res
                else:
                    print("bad response:", res.status_code)

            create_session(message.content)
            print("message content:", message.content)
            # print("request status_code:", res.status_code)
            # print("request test:", res.text)
            # print("request content:", res.content)
            # soup = BeautifulSoup(res.content, 'html.parser')
            #print(soup.prettify())
            #response = soup.prettify()
            #await message.channel.send(response)
        await self.process_commands(message)



#
#
# @bot.event
# async def on_ready():
#     print(f'{bot.user} has connected to Discord!')
#     for guild in bot.guilds:
#         print(f'{guild.name} (id: {guild.id})\n')
#
#
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
#     await bot.process_commands(message)
#
# @bot.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise


bot = CustomBot(command_prefix="!")
bot.run(TOKEN)
