import discord
import os
from discord.ext import commands
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

class datenow(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def date(self, ctx):
        import time
        import datetime
        from datetime import date
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        embed=discord.Embed(description="วันนี้วันที่เท่าไหร่กันน้า วันนี้วันที่..", color=0x00ffff)
        embed.set_author(name="Oh! Today is..", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name=(d1), value="ค่ะ!", inline=True)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('datenow plugin is ready.')

def setup(client):
    client.add_cog(datenow(client))