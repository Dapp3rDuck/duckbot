import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = 'd!')

@client.event
async def on_ready():
    print('bot is ready')

client.run(token)