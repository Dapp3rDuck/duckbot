import discord
import os
import time
import random
from discord.ext import commands

token = "NzA1NjExMDE1MjczOTcxODA0.XquNfA.rAzSDHLQRPTqlMybMSV-JoCPYlU"

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
    args = text.split(" ")
    cmd_args = []

    for x in range(2):
        cmd_args.append(args.pop(-1))

    delay = int(cmd_args[0])
    repeat = int(cmd_args[1])

    for x in range(repeat):
        time.sleep(delay)
        await ctx.send(' '.join(args))

client.run(token)