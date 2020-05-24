import discord
import os.path
from discord.ext import commands
from discord.utils import get

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def whitelist(self, msg, mc_username, user):
        channel = self.client.get_channel(707777532555952158)
        await channel.send(f"whitelist add {mc_username}")
        await msg.send(f"Registered {str(user)} as {mc_username}")
        await msg.send("Join the Minecraft server with ip: **dapp3rcraft.com**")

    @commands.command()
    async def register(self, msg):
        oldname = ""
        user = msg.message.author
        role = get(user.guild.roles, name="Members")
        mc_username = msg.message.content.replace("d!register ", "")
        path = os.path.dirname(__file__)
        f = open(f"{path}/../registered.txt", "a")
        list = open(f"{path}/../registered.txt", "r").readlines()
        already_registered = False

        for x in range (len(list)):
            if (list[x].split(" ")[0] == str(msg.message.author.id)):
                already_registered = True
                oldname = list[x].split(" ")[1]
    
        if already_registered == False:
            await user.add_roles(role)
            if mc_username != "d!register":
                await self.whitelist(msg, mc_username, user)
                f.write(f"{msg.message.author.id} {mc_username}\n")
            else:
                await msg.send("Registered " + str(user))
                f.write(f"{msg.message.author.id} \n")
            f.close()
        elif (oldname != mc_username + "\n") and (mc_username != "d!register"):
            console_channel = self.client.get_channel(707777532555952158)
            await console_channel.send(f"whitelist remove {oldname}")
            await self.whitelist(msg, mc_username, user)
            new_line = str(msg.message.author.id)
            lines = open("registered.txt", "r").readlines()
            with open("registered.txt", "w") as z:
                for line in lines:
                    if line.split(" ")[0] != new_line:
                        z.write(line)
            open("registered.txt", "a").write(f"{msg.message.author.id} {mc_username}\n")
        else:
            await msg.send("You are already registered!")

def setup(client):
    client.add_cog(Register(client))
