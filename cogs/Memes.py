import discord
import validators
import random
import os.path
from discord.ext import commands

class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def addmeme(self, msg):
        try: url = msg.message.attachments[0].url
        except: url = msg.message.content.replace("d!addmeme ", "")
        if validators.url(url):
            path = os.path.dirname(__file__)
            open(f"{path}/../memes.txt", "a").write('\n' + url)
            await msg.send('Added to meme database.')
        else: await msg.send('INVALID LINK')

    @commands.command()
    async def meme(self, msg):
        path = os.path.dirname(__file__)
        memes = open(f"{path}/../memes.txt", "r").readlines()
        await msg.send(self.get_rand_element(memes))

    def get_rand_element(self, arr):
        return arr[random.randint(0, len(arr) - 1)]

def setup(client):
    client.add_cog(Memes(client))