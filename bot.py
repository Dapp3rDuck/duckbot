import os
import os.path
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

@client.event
async def on_member_remove(member):
    print(f"{member.id} left the server.")

    registered = open("registered.txt", "r").readlines()

    for user in registered:
        user = user.split(" ")
        discord_id = user[0]
        mc_username = user[1]

        if int(discord_id) == member.id:
            console = client.get_channel(707777532555952158)
            general  = client.get_channel(361645469094379522)
            await console.send(f"whitelist remove {mc_username}")
            print(f"{discord_id} has been removed from the whitelist.")
            await general.send(f"{member.nick} left the server :[")
            new_line = str(discord_id) + " " + mc_username
            with open("registered.txt", "r") as f:
                lines = f.readlines()
            with open("registered.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != new_line:
                        f.write(line)

@client.event
async def on_member_join(member):
    pass

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))