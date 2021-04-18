import random
from pathlib import Path
import discord
import asyncio
from asyncio import sleep
import mutagen
from mutagen.mp3 import MP3
from discord.ext import commands
from discord import FFmpegPCMAudio

TOKEN = '[TOKEN]'

bot = commands.Bot(command_prefix=';') # Выбор символа префикса для ввода команд

@bot.command(name='oink', aliases=['Oink'], pass_context=True, case_insensitive=True) # Сама команда которая вводится в чат
async def oink(ctx):
        channel = ctx.message.author.voice.channel # Упрощаем жизнь и получаем channel
        voice = await channel.connect() # Аналогично с голосом
        file_path = random.choice(list(Path("/root/discord-bot/sounds/oink").glob("*.mp3"))) # С помощью рандома выбираем случайный файл из папки 
        source = FFmpegPCMAudio(str(file_path.resolve())) # Загоняем его в ffmpeg
        audio = MP3(file_path) # Получаем данные о полученном mp3
        timer = audio.info.length # Задаем его длину таймером
        player = voice.play(source, after=None) # Само проигрывание файла
        await asyncio.sleep(timer) # Здесь бот с момента входа отсчитывает длительность файла
        await voice.disconnect() # И по завершение проигрывания выходит, рекомендуется делать файлы с тишиной в начале/конце аудио.
        
@bot.command(name='barglador', aliases=['Barglador', 'BARGLADOR'], pass_context=True, case_insensitive=True) 
async def barglador(ctx):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("/root/discord-bot/sounds/barglador/BARGLADOR.mp3")
        audio = MP3("/root/discord-bot/sounds/barglador/BARGLADOR.mp3")
        timer = audio.info.length
        player = voice.play(source, after=None)
        await asyncio.sleep(timer)
        await voice.disconnect()

@bot.command(pass_context=True) # Команда на случай если бот застрянет
async def leave(ctx):
      await ctx.voice_client.disconnect()

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.run(TOKEN) # Непосредственный запуск
