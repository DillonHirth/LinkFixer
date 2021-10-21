"""os module for .env file"""
from discord.ext import commands
from bot_src.url import get_url_src


class CustomBot(commands.Bot):
    """os module for .env file2"""

    async def on_ready(self):
        """os module for .env file"""
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(f'{guild.name} (id: {guild.id})\n')

    async def on_message(self, message):
        """os module for .env file"""
        if message.author == self.user:
            return
        if 'ifunny.co' in message.content:
            print("message content:", message.content)
            response = get_url_src(message.content)
            await message.channel.send(response)
        await self.process_commands(message)
