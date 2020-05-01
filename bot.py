import discord
import os
import time
import random
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = 'd!')
client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you beans"))

def isfloat(val):
    try:
        float(val)
    except ValueError:
        return False
    return True

def isint(val):
    try:
        int(val)
    except ValueError:
        return False
    return True

async def error(context, err):
    await context.send(f"```ERROR: {err}```")

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
    msg = text.split(" ")
    cmd_args = []

    if len(msg) > 2:
        for x in range(2):
            cmd_args.append(msg.pop(-1))
            
        if isfloat(cmd_args[0]) and isint(cmd_args[1]):
            
            delay = float(cmd_args[0])
            repeat = int(cmd_args[1])

            for x in range(repeat):
                time.sleep(delay)
                await ctx.send(' '.join(msg))
    
        else:
            error(ctx, 'd!spam [message] [num of messages] [delay]')

    else:
        error(ctx, 'd!spam [message] [num of messages] [delay]')

client.run(token)