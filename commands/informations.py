import discord
from discord import app_commands
from discord.ext import commands

# Criando a classe de Moderação
class Informations(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        super().__init__()

    # Slash command para mostrar as informações do usuário
    

# Importando a classe para o arquivo main
async def setup(client):
    await client.add_cog(Informations(client))