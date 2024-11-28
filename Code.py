import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import requests
import os

intent = discord.Intents.default()
intent.members = True


client = commands.Bot(command_prefix = "!",intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready")
    print("------------------")


cogs = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cogs.append("cogs." + filename[:-3])


print(cogs)


client.run('token here')