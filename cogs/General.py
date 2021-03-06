import discord
import os.path
import random
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        path = os.path.dirname(__file__)
        self.client = client
        self.insults = open(f"{path}/../insults.txt", "r").readlines()
        self.compliments = open(f"{path}/../compliments.txt", "r").readlines()

    @commands.command()
    async def insult(self, msg, *, text):
        rand_insult = self.get_rand_element(self.insults)
        await msg.send(f"{text} {rand_insult}")

    @commands.command()
    async def compliment(self, msg, *, text):
        rand_compliment = self.get_rand_element(self.compliments)
        await msg.send(f"{text} {rand_compliment}")
    
    @commands.command()
    async def ping(self, msg):
        await msg.send(f"{round(self.client.latency * 1000)}ms")

    @commands.command()
    async def invite(self, msg):
        embed = discord.Embed(
            title="Invite",
            description="Invite the bot [**here**](https://discord.com/api/oauth2/authorize?client_id=707128143349022820&permissions=8&scope=bot)."
        )
        await msg.send(embed=embed)

    def get_rand_element(self, arr):
        return arr[random.randint(0, len(arr) - 1)]

def setup(client):
    client.add_cog(General(client))