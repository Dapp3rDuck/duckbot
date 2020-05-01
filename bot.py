import os
import time
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

helpInfo = {
    "help": "does this.", 
    "ping": "shows your ping.", 
    "spam": "spams a message.", 
    "stop": "stops spamming... maybe."
}

dospam = False
insults = open("insults.txt", "r").readlines()

load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = "d!")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you beans"))

@client.command()
async def help(msg):

    info = "```DuckBot Help\n--}=========>\n"
    for command in helpInfo:
        info += f"{command} - {helpInfo[command]}"

    await msg.send(info)

@client.command()
async def ping(msg):
    await msg.send(f"{round(client.latency * 1000)}ms")

@client.command()
async def spam(msg, *, text):
    global dospam
    dospam = True
    while dospam:
        time.sleep(1)
        await msg.send(text)

@client.command()
async def stop(msg):
    global dospam
    dospam = False

@client.command()
async def insult(msg, *, text):
    await msg.send(f"{text} {insults[random.randint(0, 3)]}")

client.run(token)