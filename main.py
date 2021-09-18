import discord
from discord import channel
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(881868600711995433)
    await channel.send(F'{member} join')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(881868600711995433)
    await channel.send(F'{member} leave')

bot.run('NzMzNTU0NzI5OTY3MTU3MzAw.XxE2FA.NG8Q_nf17VmshoC5S7SSecFs1EE')