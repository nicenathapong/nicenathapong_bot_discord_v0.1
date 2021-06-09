import discord
import os
import random
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

class mypic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def upic(self, ctx):
        responsesp = ["https://i.pinimg.com/originals/99/9c/97/999c9771fac7bb51fc4c9b8810fd53e8.png",
                    "https://i.pinimg.com/originals/cc/1b/20/cc1b2021612c6635007e18ecdd746c90.jpg",
                    "https://static.wikia.nocookie.net/virtualyoutuber/images/8/8b/Minato_Aqua_Portrait.png/revision/latest?cb=20190215180705",
                    "https://pbs.twimg.com/media/En0o0JRUcAEdO7L.jpg",
                    "https://pbs.twimg.com/media/ENJOf5eW4AACsAH.png",
                    "https://shop.dexclub.com/photo/photo_product/12320201201214712.jpg",
                    "https://otsukai.com/public/itemOrderNegotiation/110303/6049d9e69b2cf.jpeg?operation=resize&w=960",
                    "https://preview.redd.it/4cjbq7uqqhp51.jpg?width=926&format=pjpg&auto=webp&s=0f944d4fe029839f48c19148f425b810f0862b19",
                    "https://pbs.twimg.com/profile_images/1280352452487725056/pArsyieG_400x400.jpg",
                    "https://pbs.twimg.com/profile_images/1295062768559824897/bk9Pn2iS_400x400.jpg",
                    "https://pbs.twimg.com/media/Ega5CsoXgAAW_u1.png",
                    "https://i.pinimg.com/originals/f0/37/52/f03752839490515d7ecd508de56dda5d.png",
                    "https://playulti.com/static/thumb/2020/9/27/attach-1603771289138.jpg",
                    "https://scontent.fbkk22-2.fna.fbcdn.net/v/t1.6435-9/123655823_1760557944120172_8708416123239745765_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=0debeb&_nc_eui2=AeFKms7w8STb0hIoRbm2wZxmtGW_ZjyCoNe0Zb9mPIKg12f3W6UDVOGgemsQuaDi1R6Mk8WV7ZuxWV6MWydLjFh6&_nc_ohc=JEPxyV6RdEEAX8w6Afw&_nc_ht=scontent.fbkk22-2.fna&oh=733c345a127340f5bf91f1cf50cad68e&oe=60D0D824",
                    "https://pbs.twimg.com/media/E1zM9YXVIAQBJ72?format=jpg&name=medium",
                    "https://pbs.twimg.com/media/E1uAmYaVgAgPZuR?format=jpg&name=large",
                    "https://pbs.twimg.com/media/E1lknOXVoAUjZau?format=jpg&name=900x900",
                    "https://pbs.twimg.com/media/E1bgJgrVIAArVwi?format=jpg&name=900x900",
                    "https://pbs.twimg.com/media/E1PpxwlUcAAjPxP?format=jpg&name=large",
                    "https://pbs.twimg.com/media/E1GrU1WVgAM8YtC?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EznRJyXUUAA9_Uc?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EziML_4VkAImrEZ?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EzeSwjUUYAAeREE?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EzSsnSSVgAMunX7?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EzPaDOBVUAAMY-l?format=jpg&name=large",
                    "https://pbs.twimg.com/media/EyU3tg4UcAAIyfa?format=jpg&name=large",
                    "https://pbs.twimg.com/media/Ex6AlAPVEAUwHGj?format=jpg&name=large",
                    "https://pbs.twimg.com/media/Ex22HOKUYAMNTPF?format=jpg&name=large",
                    "https://pbs.twimg.com/media/ExplRT8U4AUamps?format=jpg&name=large",
                    "https://pbs.twimg.com/media/ExmhVoVUYAkS1CV?format=jpg&name=large",
                    "https://pbs.twimg.com/media/ExdyFsLVEAETEZZ?format=jpg&name=small",
                    "https://pbs.twimg.com/media/ExR9QETVoAAigY4?format=jpg&name=medium",
                    "https://pbs.twimg.com/media/ExD130nVoAMYvyo?format=jpg&name=large",
                    "https://pbs.twimg.com/media/Ew-zuN7UcAYmwcT?format=jpg&name=large",
                    "https://pbs.twimg.com/media/Ewba0QSUYAIZWWB?format=jpg&name=large",
                    "https://pbs.twimg.com/media/Etc1qyqVEAQ9s5C?format=jpg&name=large",
                    "https://pbs.twimg.com/media/ErvdpBWVQAgaUZD?format=jpg&name=large",
                    "https://xn--l8ja2b6546b.com/img/minatoaqua_scissors_hand.png"]
        await ctx.send(random.choice(responsesp))

    @commands.Cog.listener()
    async def on_ready(self):
        print('mypic plugin is ready.')

def setup(client):
    client.add_cog(mypic(client))