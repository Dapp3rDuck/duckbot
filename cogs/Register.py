import discord
from discord.ext import commands
from discord.utils import get

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Register for Dapp3rCraft
    @commands.command()
    async def register(self, msg):
        user = msg.message.author
        role = get(user.guild.roles, name="Members")
        mc_username = msg.message.content.replace("d!register ", "")
        await user.add_roles(role)
        if mc_username != "d!register":
            self.whitelist(msg, mc_username, user)
        else:
            await msg.send("Registered " + str(user))

    @commands.command()
    async def unregister(self, msg):
        user = msg.message.author
        admin_role = get(user.guild.roles, name="Admin")
        mc_username = msg.message.content.replace("d!unregister ", "")
        channel = self.client.get_channel(707777532555952158)
        if admin_role in user.roles:
            await channel.send(f"whitelist remove {mc_username}")
            await msg.send(f"**{mc_username}** has been unregistered from the Minecraft server.")
        else: 
            msg.send("You do not have permission to use this command!")

    async def whitelist(self, msg, username, user):
        channel = self.client.get_channel(707777532555952158)
        await channel.send(f"whitelist add {mc_username}")
        await msg.send(f"Registered {str(user)} as {mc_username}")

def setup(client):
    client.add_cog(Register(client))