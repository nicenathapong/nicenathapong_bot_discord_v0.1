from inspect import CO_ITERABLE_COROUTINE
import discord
import os
import sys
import time
from os.path import join, dirname
from discord.utils import get
from discord.ext import commands
from discord.ext.commands.core import command

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")

import json

with open('botconfig.json') as config_file:
    data = json.load(config_file)

token = data['token']
prefix = data['prefix']
version = data['version']
adminid = data['adminid']
adminuser = data['adminuser']

#==================================================

client = commands.Bot(command_prefix = (prefix))
client.remove_command('help')

#==================================================

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def restart(ctx):
    if ctx.author.id == data['adminid'] :
        embed=discord.Embed(title="บอท nicenathapong ได้ถูกเริ่มต้นใหม่", description=(current_time), color=0x00ffff)
        embed.set_author(name="nicenathapong bot is restart!", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)
        print('Restarting bot...')
        restart_bot()

#==================================================

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
    print('------------------------------')
    print('nicenathapong bot is startup!')
    print('------------------------------')
    print(' - ' + (version))
    print(' - release date 06/06/21')
    print(' - run on .python')
    print('------------------------------')
    guild = client.get_guild(845892096534904832)
    channel = guild.get_channel(846408294490832918)
    embed=discord.Embed(title="บอท nicenathapong ได้ถูกรันแล้ว", description=(current_time), color=0x00ffff)
    embed.set_author(name="nicenathapong bot is startup!", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
    embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
    await channel.send(embed=embed)
    print('------------------------------')
    print('12 plugins is already installed!')
    print('------------------------------')
    print('Delete junk files...')
    os.system('deletejunk.bat')
    print('------------------------------')
    print('Servers list now :')
    for guild in client.guilds:
        print(guild.name)
    print('------------------------------')
    print(f"Total server is : {len(client.guilds)} servers!")
    print('------------------------------')

#==================================================

client.run(token)