import discord
import os
import time
import asyncio
import youtube_dl
from os.path import join, dirname
from discord.utils import get
from discord.ext import commands
from discord.ext.commands.core import command
from datetime import datetime

import json

with open('../bot/botconfig.json') as config_file:
    data = json.load(config_file)

token = data['token']
prefix = data['prefix']
version = data['version']
adminid = data['adminid']
adminuser = data['adminuser']

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

#==================================================

class playsong(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='p', help='This command plays music')
    async def p(self, ctx, url):
        if not ctx.message.author.voice:
            embed=discord.Embed(description="You are not connected to a voice channel!", color=0x00ffff)
            embed.set_author(name="nicenathapong bot 🎶 music player", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
            embed.add_field(name="คุณไม่ได้อยู่ในห้องพูดคุยเสียงนะคะ?", value="ต้องอยู่ในห้องพูดคุยก่อนถึงจะเปิดเพลงได้น้า", inline=True)
            embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
            await ctx.send(embed=embed)

            return

        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(url)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        embed=discord.Embed(description="เรากำลังเปิดเพลงให้คุณฟังค่ะ!", color=0x00ffff)
        embed.set_author(name="nicenathapong bot 🎶 music player", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name="Now playing :", value=('{}'.format(player.title)), inline=True)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()

    @commands.Cog.listener()
    async def on_ready(self):
        print('playsong plugin is ready.')

def setup(client):
    client.add_cog(playsong(client))