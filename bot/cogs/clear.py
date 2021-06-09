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

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    def admin(ctx):
        return ctx.message.author.id == (adminid)
        
    @commands.command()
    @commands.check(admin)
    async def c(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send('**==========================================**')

    @commands.command()
    @commands.check(admin)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send('**==========================================**')

    @commands.Cog.listener()
    async def on_ready(self):
        print('clear plugin is ready.')
        
def setup(client):
    client.add_cog(clear(client))