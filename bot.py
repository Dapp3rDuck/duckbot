import discord
import os
import time
import random
from discord.ext import commands
from dotenv import load_dotenv

dospam = False

f = open("insults.txt", "r")
insults = f.readlines()

load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = 'd!')
client.remove_command('help')

@client.event
async def on_ready():
    print('bot is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you beans"))

@client.command()
async def help(ctx):
    await ctx.send("```DuckBot Help\n--}=========>\nhelp - does this\nping - shows your ping\nspam - spams a message\nstop - stops spamming, mabey```")

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def spam(ctx, *, text):
    global dospam
    dospam = True
    while dospam:
        time.sleep(1)
        await ctx.send(text)

@client.command()
async def stop(ctx):
    global dospam
    dospam = False

@client.command()
async def insult(ctx, *, text):
    await ctx.send(text + " " + insults[random.randint(0,3)])

client.run(token)