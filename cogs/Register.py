import discord
from discord.ext import commands

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Register for Dapp3rCraft
    @client.command()
    async def register(self, msg, *, text):
        pass

def setup(client):
    client.add_cog(Register(client))