import discord
from discord.ext import commands

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Register for Dapp3rCraft
    @commands.command()
    async def register(self, msg):
        user = msg.message.author
        role = get(user.server.roles, name="Members")
        console = client.get_channel(707777532555952158)
        await client.add_roles(user, role)
        await console.send('whitelist add ' + msg)
        await msg.send('Registered ' + self + ' as ' + msg)

def setup(client):
    client.add_cog(Register(client))