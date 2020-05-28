import discord
import validators
import random
import os.path
from config import info
from discord.ext import commands

class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def addmeme(self, msg):
        server = msg.message.server
        if True:   
            try: 
                url = msg.message.attachments[0].url
            except: 
                url = msg.message.content.replace("d!addmeme ", "")
            path = os.path.dirname(__file__)
            if validators.url(url):
                memes = open(f"{path}/../memes/{server}.txt", "r").readlines()
                duplicate = False
                for x in range (len(memes)):
                    if (memes[x] == url + "\n"):
                        duplicate = True
                if duplicate == False:
                    open(f"{path}/../memes/{server}.txt", "a").write("\n" + url)
                    await msg.send("Added to meme database.")
                else:
                    await msg.send("I already have that meme!")
            else: 
                await msg.send("Invalid Link!")
        else:
            return await msg.send("You do not have permissions to use this command!")

    @commands.command()
    async def meme(self, msg):
        path = os.path.dirname(__file__)
        server = server.id
        try:
            memes = open(f"{path}/../memes/{server}.txt", "r").readlines()
            rand_meme = self.get_rand_element(memes)
            await msg.send(rand_meme)
        except:
            await msg.send("I don't have any memes yet!\nAdd one with `d!addmeme`")

    def get_rand_element(self, arr):
        return arr[random.randint(0, len(arr) - 1)]

def setup(client):
    client.add_cog(Memes(client))