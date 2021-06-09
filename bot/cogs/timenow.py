import discord
import os
from discord.ext import commands
from datetime import datetime
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

class timenow(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def time(self, ctx):
        import time
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        embed=discord.Embed(description="เวลาในตอนนี้ก็คือ..", color=0x00ffff)
        embed.set_author(name="Oh! Time now is..", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name=(current_time), value="นาฬิกา ค่ะ!", inline=True)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('timenow plugin is ready.')

def setup(client):
    client.add_cog(timenow(client))