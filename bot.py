"""
Awesomebot entry point
Mike Tung (seekheart)
"""

import discord
import asyncio
from settings import CREDS, PREFIX, logger



def init_bot():
    """Creates a discord client connection"""
    return discord.Client()

client = init_bot()

@client.event
async def on_ready():
    """Logs the bot in for operations"""
    print('logged in as {}'.format(client.user.name))

if __name__ == '__main__':
    client.run(CREDS['token'])
