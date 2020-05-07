import discord
from discord.ext import commands
from config import info

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.info = info.help

    @commands.command()
    async def help(self, msg):

        embed = discord.Embed(
            title="DuckBot Help", 
            description="[**GitHub**](https://www.github.com/dapp3rduck/duckclient)"
        )

        for command in self.info:
            embed.add_field(
                name=f"d!{command}",
                value=self.info[command], 
                inline=False
            )

        await msg.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))