import discord
import os.path
import random
from config import info
from discord.utils import get
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.admins = info.bot_admins
        self.console_channel = client.get_channel(707777532555952158)

    @commands.command()
    async def ban(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        mc_username = msg.message.content.replace("d!ban ", "")

        if admin_role in user.roles:
            await self.console_channel.send(f"ban {mc_username}")
            await msg.send(f"**{mc_username}** has been banned.")
        else: 
            await msg.send("You do not have permission to use this command!")

    @commands.command()
    async def unban(self, msg):
        user = msg.message.author
        mc_username = msg.message.content.replace("d!unban", "")

        if admin_role in user.roles: 
            await self.console_channel.send(f"unban {mc_username}")
            await msg.send(f"**{mc_username}** has been unbanned.")
        else: 
            await msg.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Admin(client))