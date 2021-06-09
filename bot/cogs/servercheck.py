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

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    def nicenathapong(ctx):
        return ctx.author.id == (adminid)

    @commands.command()
    @commands.check(nicenathapong)
    async def sva(self, ctx):
        await ctx.send('==========================================')
        await ctx.send('**Servers list now is:**')
        for guild in self.client.guilds:
            await ctx.send(guild.name)
        await ctx.send('==========================================')
        embed=discord.Embed(description="ดิสที่ฉันอยู่ในตอนนี้ตอนนี้ มีทั้งหมด", color=0x00ffff)
        embed.set_author(name="Um... Servers count now is..", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name=len(self.client.guilds), value="ดิสค่ะ เยอะมั้ยคะ..555", inline=True)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('clear plugin is ready.')
        
def setup(client):
    client.add_cog(clear(client))