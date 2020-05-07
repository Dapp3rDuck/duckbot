import discord
from discord.ext import commands

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Register for Dapp3rCraft
    @commands.command()
    async def register(self, msg):
        await msg.send('Registered')
        channel = client.get_channel(707777532555952158)
        await channel.send('whitelist add ' + msg)
        return

def setup(client):
    client.add_cog(Register(client))