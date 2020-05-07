import discord
from discord.ext import commands
from discord.utils import get

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Register for Dapp3rCraft
    @commands.command()
    async def register(self, msg):
        user = msg.message.author
        role = get(user.guild.roles, name="Members")
        await user.add_roles(role)
        channel = self.client.get_channel(707777532555952158)
        await channel.send('hello')
        await msg.send('Registered ' + self + ' as ' + msg)

def setup(client):
    client.add_cog(Register(client))