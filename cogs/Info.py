import discord
from discord.ext import commands
from config import info

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.info = info.help

    @commands.command()
    async def help(self, msg):
        helpEmbed = discord.Embed(
            title="DuckBot Help", 
            description="[**dapp3rcraft.com**](http://www.dapp3rcraft.com/)"
        )
        for cmd in self.info:
            helpEmbed.add_field(
                name=f"d!{cmd}",
                value=self.info[cmd], 
                inline=False
            )
        await msg.send(embed=helpEmbed)

def setup(client):
    client.add_cog(Info(client))
