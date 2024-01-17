# program
import os
import logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
import discord
import logging.handlers
from datetime import datetime
now = datetime.now()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('>time'):
        await message.channel.send(now)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('>help'):
        await message.channel.send(">hello - Prints an hello.                                        "
                                   
                                   ">time - Tells the time")

client.run('MTE4NjM0MDU2OTM4ODE2NzMzMA.GUCudL.KZbSMIeHCvlM8SUdFew5bNaw2fduFe_qx1WF2A', log_handler=None)