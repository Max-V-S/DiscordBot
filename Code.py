import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import requests


intent = discord.Intents.default()
intent.members = True


client = commands.Bot(command_prefix = "!",intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready")
    print("------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, this is the server bot!")

#Rolls a random number between 1 and 10
@client.command()
async def roll(ctx, amount):
    dice_roll = random.randint(1,int(amount))
    await ctx.send(dice_roll)


@client.event
async def on_member_join(member):
    channel = client.get_channel(1303936958749212697)
    await channel.send("Hello")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(1303936958749212697)
    await channel.send("Cya")

#Start of audio commands
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        await ctx.send("joining voice channel")
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Lil Uzi Vert - Grow Up.mp3')
        player = voice.play(source)

    else:
        await ctx.send("Unable to join: you must be in a voice channel")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Leaving voice channel")
    else:
        await ctx.send("I am not in any voice channels")


@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Audio is now paused")
    else:
        await ctx.send("No audio is playing right now")


@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is currently playing")


@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    voice.stop()


@client.command(pass_context = True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg)
    player = voice.play(source)
#End of audio commands

#Now Detecting Specific Words
@client.event
async def on_message(message):
    if message.content == "bad message":
        await message.delete()
        await message.channel.send("Don't send bad messages!!!")
#End


@client.command()
async def embed(ctx):
    embed = discord.Embed(title = "Dog", url = "https://google.com", description = "We love dogs!", color = 0x34ebc3)
    await ctx.send(embed = embed)

client.run("put token here")


