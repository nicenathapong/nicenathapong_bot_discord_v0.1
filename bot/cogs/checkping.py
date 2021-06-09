import discord
import os
from discord.ext import commands
from discord.ext.commands.core import command
from os.path import join, dirname

import json

with open('../bot/botconfig.json') as config_file:
    data = json.load(config_file)

token = data['token']
prefix = data['prefix']
version = data['version']
adminid = data['adminid']
adminuser = data['adminuser']

#==================================================

class checkping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(description="ตอนนี้ปิงของบอทอยู่ที่..", color=0x00ffff)
        embed.set_author(name="pong! now bot ping is..", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name=round(self.client.latency * 1000), value="millisecond ค่ะ!", inline=True)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('checkping plugin is ready.')

def setup(client):
    client.add_cog(checkping(client))