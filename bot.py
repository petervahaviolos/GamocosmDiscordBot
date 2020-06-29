import datetime
import sys
from os.path import isdir
from secrets_file import bot_token

import discord
from discord.ext import commands, timers
from discord.utils import find, get

client = commands.Bot(command_prefix='!')
old_roles = {}


@client.event
async def on_ready():
    print('Bot online')

initial_extensions = ['server']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}", file=sys.stderr)


client.run(bot_token)