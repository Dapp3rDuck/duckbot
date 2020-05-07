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
        mc_username = msg.message.content.replace("d!register ", "")
        await user.add_roles(role)
        await self.client.get_channel(707777532555952158).send(f"whitelist add {mc_username}")
        await msg.send('Registered ' + str(user) + ' as ' + mc_username)

def setup(client):
    client.add_cog(Register(client))