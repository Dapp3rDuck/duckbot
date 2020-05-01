import os
import time
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from config import info

helpInfo = info.help

dospam = False
insults = open("insults.txt", "r").readlines()
compliments = open("compliments.txt", "r").readlines()

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

    info = "```----------- DuckBot Help ------------\nhttps://github.com/Dapp3rDuck/duckbot\n-------------------------------------\n"
    for command in helpInfo:
        info += f"{command} - {helpInfo[command]}\n"
    info += '```'

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
    await msg.send(f"{text} {insults[random.randint(0, (len(insults)-1))]}")

@client.command()
async def compliment(msg, *, text):
    await msg.send(f"{text} {compliments[random.randint(0, (len(compliments)-1))]}")

client.run(token)