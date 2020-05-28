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

    def get_rand_element(self, arr):
        return arr[random.randint(0, len(arr) - 1)]

def setup(client):
    client.add_cog(General(client))