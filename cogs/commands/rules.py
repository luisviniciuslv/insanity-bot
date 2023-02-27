import discord
from colorize import colorize_rainbow
from discord.ext import commands

class Rules(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def rules(self, ctx):
    embed=discord.Embed(title="Regras do servidor")
    embed.add_field(name="Regra 1", value="regra aqui", inline=False)
    embed.add_field(name="Regra 2", value="regra aqui", inline=False)
    await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(Rules(client))
