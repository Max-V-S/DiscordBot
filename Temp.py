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
    await client.process_commands(message)
    if "bad message" in message.content:
        await message.delete()
        await message.channel.send("Don't send harmful messages!!!")
#End


#Provides an embedded message for chunks of quick information
@client.command()
async def python(ctx):
    embed = discord.Embed(title = "I LOVE PYTHON", url = "https://www.python.org/downloads/", description = "It's great!", color = 0x34ebc3)
    embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq0Pw0WiD1CJI4ZKFwmjP9uaatqk5ICQSglA&s")
    await ctx.send(embed = embed)


@client.command()
async def embed(ctx):
    embed = discord.Embed(title = "I LOVE PYTHON", url = "https://www.python.org/downloads/", description = "It's great!", color = 0x34ebc3)
    embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq0Pw0WiD1CJI4ZKFwmjP9uaatqk5ICQSglA&s")
    embed.add_field(name = "Field 1", value = "test value", inline = True)
    embed.add_field(name = "Field 2", value = "test value", inline = True) #Inline True == same line / Inline False == seperate lines
    embed.set_footer(text = "End of embed")
    await ctx.send(embed = embed)
#possible ideas for enbeds: create an imbed for each element on the periodic table using dictionaries


#Error checking
@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("No permission to run")



#Reactions
@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(user.name + " added a " + reaction.emoji)

@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    await channel.send(user.name + " removed a " + reaction.emoji)
#Idea: create a blackjack game that holds or hits based on the reaction given





client.run()


