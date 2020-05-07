import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="d!")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name="you beans"
        )
    )

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))