import random
from pathlib import Path
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

TOKEN = '[TOKEN]'

bot = commands.Bot(command_prefix=';')

@bot.command(name='oink', aliases=['Oink'], pass_context=True, case_insensitive=True)
async def oink(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        file_path = random.choice(list(Path("/root/discord-bot/sounds/oink").glob("*.mp3")))
        source = FFmpegPCMAudio(str(file_path.resolve()))
        player = voice.play(source, after=None)

@bot.command(name='barglador', aliases=['Barglador', 'BARGLADOR'], pass_context=True, case_insensitive=True)
async def barglador(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("/root/discord-bot/sounds/barglador/BARGLADOR.mp3")
        player = voice.play(source, after=None)

@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)
