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

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    def nicenathapong(ctx):
        return ctx.author.id == 635750674604359690

    @commands.command()
    @commands.check(nicenathapong)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(title=(member), description="ได้ถูกแบนจากดิสนี้ค่ะ.. ;w;")
        embed.set_author(name="Oh..so sad...", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_footer(text="bot by nicenathapong | " + (version) + " | run on .python")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('ban plugin is ready.')

def setup(client):
    client.add_cog(ban(client))