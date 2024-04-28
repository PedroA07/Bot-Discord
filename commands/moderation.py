import discord
from discord import app_commands
from discord.ext import commands

# Criando a classe de Moderação
class Moderations(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        super().__init__()

    # Slash command para Limpar o chat
    @app_commands.command(name="limpar", description="Limpa o chat.") # Definindo nome e descrição
    @app_commands.describe(quantidade="Escolha a quantidade de mensagens à serem apagadas.") # Definindo descrição do argumento
    async def limpar(self, interaction: discord.Interaction, quantidade: int): # Criando a função
        if not interaction.user.guild_permissions.manage_permissions: # verificando Permissões
            # Criando Embed para eviar a mensagem
            embed = discord.Embed(
                title="🚨 PERMISSÃO NEGADA!",
                description="Apenas **Administradores e Moderadores** podem utilizar este comando!",
                color= discord.Color.red(),
            )
            return interaction.response.send_message(embed=embed, ephemeral=True)
        if quantidade > 100 or quantidade < 1: # Definindo os limites de menssagens que podem ser apagadas
            # Criando Embed para eviar a mensagem
            embed = discord.Embed(
                title=":warning: QUANTIDADE INVÁLIDA!",
                description=f"**Valor inserido:** ` {quantidade} `\n\n"
                f"A quantidade de mensagens não podem ser **menor que 1**, ou **maior que 100**.\n\n"
                "Por favor insíra um número válido!",
                color= discord.Color.yellow(),
            )
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.defer() # Prolongando o tempo de resposta para caso demore o processo
            msg_limpas = await interaction.channel.purge(limit=int(quantidade)) # Apagando as mensagens
            # Criando Embed para eviar a mensagem
            embed = discord.Embed(
                title="✅ CHAT LIMPO!",
                description=f"O chat teve ` {len(msg_limpas)} ` de mensagens apagadas!",
                color= discord.Color.blue(),
                timestamp=interaction.created_at
            )
            embed.set_footer(text = f"Por: **{interaction.user.name}**")
            await interaction.channel.send(embed=embed) # Enviando mensagem de confirmação


# Importando a classe para o arquivo main
async def setup(client):
    await client.add_cog(Moderations(client))