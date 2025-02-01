# Koi bot - por: Vinícius

# Importando dependencias
import os
import logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
import discord
import logging.handlers
from datetime import datetime
now = datetime.now()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
token = os.environ["DISCORD_TOKEN"]
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# Confirma que o bot iniciou
@client.event
async def on_ready():
    print(f'Logado como: {client.user}')

# Comandos abaixo
# >hello:. Manda um olá em inglês.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        await message.channel.send('Hello!')
# >time: Manda o tempo atual do sistema do servidor
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('>time'):
        await message.channel.send(now)

# >help: Manda uma mensagem com os comandos que o bot tem
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('>help'):
        await message.channel.send(">hello - Prints an hello."
                                   ">time - Tells the time")
# Inicia o bot
client.run(token, log_handler=None)
