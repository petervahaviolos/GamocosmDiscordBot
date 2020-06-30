import datetime
import sys
import os
import logging
import confuse
from server import Server
from os.path import isdir

import discord
from discord.ext import commands
from discord.utils import find, get

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler('app.log'), logging.StreamHandler(sys.stdout)],
                    format='[%(asctime)s %(levelname)s] %(message)s')
logging.info("------APP STARTED------")

config = confuse.Configuration('MinecraftDiscordBot', __name__)

# configtemplate = {
#     'serverId': str,
#     'apiKey': str,
#     'discordKey': str,
#     'commandPrefix': str,
#     'description': str
# }

logging.info(f"Config: {config.items}")
SERVER_ID = config['serverId'].get()
API_KEY = config['apiKey'].get()
DISCORD_KEY = config['discordKey'].get()
COMMAND_PREFIX = config['commandPrefix'].get()
DESCRIPTION = config['description'].get()

server = Server(SERVER_ID, API_KEY)
logging.info(f"Starting status is: {server._status()}")

client = commands.Bot(command_prefix=COMMAND_PREFIX if COMMAND_PREFIX != "" else "!",
                      description=DESCRIPTION)

initial_extensions = ['cogs.admin']


@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n")
    logging.info(f"Successfully logged in and running")

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            logging.error(f"Failed to load extension {extension}", file=sys.stderr)


client.run(DISCORD_KEY)