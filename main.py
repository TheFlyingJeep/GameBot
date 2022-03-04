import discord
from discord.ext import commands
import youtube_dl
import urllib.parse, urllib.request, re
import requests
import utilFunctions as uf
import os
import asyncio


client = commands.Bot(command_prefix="!")
with open("token.txt", "r") as t:
    token = t.read()
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }


@client.event
async def on_ready():
    print("I am online from here?")


@client.command()
async def minigames(ctx):
    try:
        games = ctx.message.content.split()[1]
    except IndexError:
        games = 5

@client.command()
async def download(ctx, *, search):
    link = urllib.parse.urlencode({'search_query': search})
    content = urllib.request.urlopen('http://www.youtube.com/results?' + link)
    searchresult = re.findall(r'/watch\?v=(.{11})', content.read().decode())
    url = ('http://www.youtube.com/watch?v=' + searchresult[0])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    await ctx.send("Downloaded " + info["title"])


client.run(token)
