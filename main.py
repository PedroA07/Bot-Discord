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
intents.members = True # Necessário para receber eventos de membros

# Criar o bot com os intents
client = commands.Bot(command_prefix='/', intents=intents)

# Função para carregar os cogs de uma categoria
async def load_cogs():
    for filename in os.listdir('commands'): # Aqui ele vai percorrer pelos arquivos que estão dentro da pasta commands
        if filename.endswith('.py'): # Criando regra para ler apenas os arquivos que terminam com .py
            await client.load_extension(f'commands.{filename[:-3]}') # Aqui ele vai ignorar os últimos 3 digitos do nome do arquivo, para poder ler o código

# Commando de sincronização de slash commands
@client.command()
async def sinc(ctx: commands.Context):
    if ctx.author.guild_permissions.administrator: # Verificando permissão de cargo
        sincs = await client.tree.sync()
        # Criando Embed para eviar a mensagem
        embed = discord.Embed(
            title= "✅ SINCRONIZADO COM SUCESSO!",
            description= f"{len(sincs)} de comandos foram sincronizados por {ctx.author.mention}!",
            color= discord.Color.green(),
            timestamp= ctx.message.created_at
        )
        await ctx.reply(embed=embed)
    else:
        # Criando Embed para eviar a mensagem
        embed = discord.Embed(
            title= "🚨 COMANDO NEGADO!",
            description= "Apenas administradores podem usar o commando!",
            color= discord.Color.red(),
            timestamp= ctx.message.created_at
        )
        ctx.reply()

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