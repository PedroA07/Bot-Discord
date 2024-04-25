import discord
from discord.ext import commands
from discord import app_commands
import os
from colorama import Fore, Back, Style
import time
import platform
from dotenv import load_dotenv

# Carrega o token do bot a partir de um arquivo de configuração separado
load_dotenv()

# Definindo os intents necessários
intents = discord.Intents.default()
intents.message_content = True  # Necessário para receber eventos de mensagens
intents.members = True

# Criar o bot com os intents
client = commands.Bot(command_prefix='/', intents=intents)

# Função para carregar os cogs de uma categoria
async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

# Commando de sincronização de slash commands
@client.command()
async def sinc(ctx: commands.Context):
    if ctx.author.guild_permissions.administrator:
        sincs = await client.tree.sync()
        await ctx.reply(f"{len(sincs)} de comandos foram sincronizados!")
    else:
        ctx.reply("Apenas administradores podem usar o commando!")

# Evento para indicar que o client está pronto
@client.event
async def on_ready():
    await load_cogs()
    prfx = (Back.BLACK + Fore.GREEN + time.strftime('%H:%M:%S UTC', time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + " Logado como: " + Fore.YELLOW + client.user.name)
    print(prfx + " Bot ID: " + Fore.YELLOW + str(client.user.id))
    print(prfx + " Discord Version: " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version: " + Fore.YELLOW + str(platform.python_version()))

# Carrega o TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')
# Executa o client
client.run(TOKEN)