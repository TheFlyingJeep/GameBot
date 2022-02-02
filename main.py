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


@client.command()#Can't test during school need to fix things on laptop :P
async def checkGrades(ctx):
    await ctx.send("You should check dms ;)))")
    person = ctx.author
    infomsg = await person.send("Please input your name and password :') (WILL NOT BE STORED, CHECK GITHUB FOR CONFIRMATION :'))")

    def check(user, channel):
        return user.id == person.id and channel.id == infomsg.channel.id

    try:
        info = await client.wait_for("message", timeout=30, check=check)
        if len(info) != 2:
            await person.send("You either excluded info or added too much info XD")
        else:
            blaa = info.split()
            uname, passw = blaa[0], blaa[1]
            page = requests.get("https://hcpss.instructure.com/grades")
            print(page)
            print(uname + " " + passw)
    except TimeoutError:
        await person.send("You took too long :P")



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
