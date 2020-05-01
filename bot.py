import discord
import os
import time
import random
from discord.ext import commands
from dotenv import load_dotenv

dospam = False

load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = 'd!')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

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

client.run(token)