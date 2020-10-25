import discord
import time
from discord.ext import commands

class Spam(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.dospam = False
    
    @commands.command()
    async def spam(self, msg, *, text):
        if text.find('@everyone') != -1 or text.find('@here') != -1:
            return
        
        self.dospam = True
        while self.dospam:
            time.sleep(1)
            await msg.send(text)

    @commands.command()
    async def stop(self, msg):
        self.dospam = False

def setup(client):
    client.add_cog(Spam(client))
