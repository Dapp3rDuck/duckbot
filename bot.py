import os
import time
import random
import discord
import validators

from discord.ext import commands
from dotenv import load_dotenv
from config import info

helpInfo = info.help

dospam = False
insults = open("insults.txt", "r").readlines()
compliments = open("compliments.txt", "r").readlines()

load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix="d!")
client.remove_command("help")

def get_rand_element(arr):
    return arr[random.randint(0, len(arr) - 1)]

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name="you beans"
        )
    )

@client.command()
async def help(msg):
    embed = discord.Embed(
        title="DuckBot Help", 
        description="[**GitHub**](https://www.github.com/dapp3rduck/duckbot)"
    )
    for command in helpInfo:
        embed.add_field(
            name=f"d!{command}",
            value=helpInfo[command], 
            inline=False
        )
    await msg.send(embed=embed)

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
    await msg.send(f"{text} {get_rand_element(insults)}")

@client.command()
async def compliment(msg, *, text):
    await msg.send(f"{text} {get_rand_element(compliments)}")

@client.command()
async def addmeme(msg):
    try: url = msg.message.attachments[0].url
    except: url = msg.message.content.replace("d!addmeme ", "")
    if validators.url(url):
        open("memes.txt", "a").write('\n' + url)
        await msg.send('Added to meme database.')
    else: await msg.send('INVALID LINK')

@client.command()
async def meme(msg):
    memes = open("memes.txt", "r").readlines()
    await msg.send(get_rand_element(memes))

# Register for Dapp3rCraft
@client.command()
async def register(msg, *, text):
    pass

client.run(token)