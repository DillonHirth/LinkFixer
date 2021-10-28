"""
discord.ext: part of discord.py package
    https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
"""
from discord.ext import commands
from link_fixer import url


class CustomBot(commands.Bot):
    """
    I subclassed discord.ext.commands.bot class, to override its methods.
    I primarily followed the linked tutorial below,
    but I wanted to do it differently to make sure I was thinking on my own.
    https://realpython.com/how-to-make-a-discord-bot-python/
    """

    async def on_ready(self):
        """
        override of the on_ready event, currently just a simple message outputting
        discord guilds its connected too
        """
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(f'{guild.name} (id: {guild.id})\n')

    async def on_message(self, message):
        """
        override of the on_message event
        confirms message isnt from bot, then passes the message to url.get_url_src which
        returns the direct link. that direct link is then sent to to the message channel
        """
        if message.author == self.user:
            return
        if 'https://' in message.content:
            print("message content:", message.content)
            message_url = message_parse_for_url(message.content)
            response = url.get_url_src(message_url)
            await message.channel.send(response)
            await message.delete()
        await self.process_commands(message)


def message_parse_for_url(message):
    """
    takes message string
    returns url that was within that message
    """
    # split the message.content by spaces
    message_list = message.split()
    # iterate through until i have a link
    for item in message_list:
        print(item)
        if 'https://' in item or 'ifunny.co' in item:
            return item
    return None
