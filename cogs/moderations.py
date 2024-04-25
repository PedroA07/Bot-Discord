import discord
from discord import app_commands
from discord.ext import commands

class Moderations(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        super().__init__()

    @app_commands.command()
    async def hello(self, interact: discord.Interaction):
        await interact.response.send_message("Hello!")

async def setup(client):
    await client.add_cog(Moderations(client))