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
        server = msg.guild.id
        path = os.path.dirname(__file__)
        try:    
            memes = open(f"{path}/../memes/{server}.txt", "r").readlines()
        except:
            memes = []

        try: 
            url = msg.message.attachments[0].url
        except: 
            url = msg.message.content.replace("d!addmeme ", "")
        if validators.url(url):
            duplicate = False
            for x in range (len(memes)):
                if (memes[x] == url):
                    duplicate = True
            if duplicate == False:
                open(f"{path}/../memes/{server}.txt", "a").write("\n" + url)                
                await msg.send("Added to meme database.")
            else:
                await msg.send("I already have that meme!")
        else: 
            await msg.send("Invalid Link!")

    @commands.command()
    async def meme(self, msg):
        path = os.path.dirname(__file__)
        server = msg.guild.id
        try:
            memes = open(f"{path}/../memes/{server}.txt", "r").readlines()
            rand_meme = self.get_rand_element(memes)
            await msg.send(rand_meme)
        except:
            await msg.send("I don't have any memes yet!\nAdd one with `d!addmeme`")

    def get_rand_element(self, arr):
        return arr[random.randint(1, len(arr) - 1)]

    @commands.command()
    async def memes(self, msg):
        path = os.path.dirname(__file__)
        server = str(msg.guild.id)
        try:
            memes = open(f"{path}/../memes/{server}.txt", "r").readlines()
            await msg.send(f"There are **{len(memes)-1}** memes in this server's database.")
        except:
            await msg.send("This server doesen't have any memes yet.\nAdd one with `d!addmeme`!")

def setup(client):
    client.add_cog(Memes(client))
