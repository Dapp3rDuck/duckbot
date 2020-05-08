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
        self.admin_role = get(user.guild.roles, name="Admin")

    @commands.command()
    async def ban(self, msg):
        user = msg.message.author
        console_channel = self.client.get_channel(707777532555952158)
        mc_username = msg.message.content.replace("d!ban ", "")

        if self.admin_role in user.roles:
            await console_channel.send(f"ban {mc_username}")
            await msg.send(f"**{mc_username}** has been banned.")
        else: 
            await msg.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Admin(client))