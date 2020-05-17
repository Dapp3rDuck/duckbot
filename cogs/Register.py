import discord
import os.path
from discord.ext import commands
from discord.utils import get

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def whitelist(self, msg, mc_username, user):
        channel = self.client.get_channel(707777532555952158)
        await channel.send(f"whitelist add {mc_username}")
        await msg.send(f"Registered {str(user)} as {mc_username}")
        await msg.send("Join the Minecraft server with ip: **livepond.net**")

    @commands.command()
    async def register(self, msg):
        user = msg.message.author
        role = get(user.guild.roles, name="Members")
        mc_username = msg.message.content.replace("d!register ", "")
        path = os.path.dirname(__file__)
        f = open(f"{path}/../registered.txt", "w")
        await user.add_roles(role)
        if mc_username != "d!register":
            await self.whitelist(msg, mc_username, user)
            f.write(f"{msg.message.author.id} {mc_username}")
        else:
            await msg.send("Registered " + str(user))
            f.write(f"{msg.message.author.id} ")
        f.close()

def setup(client):
    client.add_cog(Register(client))