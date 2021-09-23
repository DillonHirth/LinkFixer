from discord.ext import commands
from dotenv import load_dotenv
from url import get_url_src

load_dotenv()


class CustomBot(commands.Bot):

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(f'{guild.name} (id: {guild.id})\n')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'ifunny.co' in message.content:
            print("message content:", message.content)
            response = get_url_src(message.content)
            await message.channel.send(response)
        await self.process_commands(message)
