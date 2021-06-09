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

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(description="นี่คือคำสั่งทั้งหมดที่คุณสามารถใช้ได้นะคะ", color=0x00ffff)
        embed.set_author(name="May I help you?", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name="n.p (ชื่อเพลงในยูทูป หรือลิงก์ก็ได้นะคะ)", value="บอทจะเข้ามาเปิดเพลงที่คุณขอให้คุณฟังค่ะ!", inline=False)
        embed.add_field(name="n.stop", value="บอทจะปิดเพลง และออกจากห้องเสียงที่คุณอยู่ค่ะ", inline=False)
        embed.add_field(name="n.horo (คำถาม)", value="อยากถามอะไรถามมาได้เลยนะคะ ฉันจะทำนายให้คุณเองค่ะ!", inline=False)
        embed.add_field(name="n.time", value="อยากรู้เวลาตอนนี้หรอคะ? ใช้คำสั่งนี้ได้เลยค่ะ!", inline=False)
        embed.add_field(name="n.date", value="วันนี้วันที่เท่าไหร่น้า อยากรู้ก็ถามได้เลยนะคะ~", inline=False)
        embed.add_field(name="n.upic", value="ส่งรูปที่น่ารักๆของฉันให้คุณดูไงคะ~ (minato aqua)", inline=False)
        embed.add_field(name="n.ping", value="ตรวจสอบความหน่วงของตัวฉันเองค่ะ", inline=False)
        embed.add_field(name="n.help", value="ดูว่าตัวฉันสามารถทำอะไรได้บ้าง (ในตอนนี้)", inline=False)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.command()
    async def h(self, ctx):
        embed=discord.Embed(description="นี่คือคำสั่งทั้งหมดที่คุณสามารถใช้ได้นะคะ", color=0x00ffff)
        embed.set_author(name="May I help you?", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name="n.p (ชื่อเพลงในยูทูป หรือลิงก์ก็ได้นะคะ)", value="บอทจะเข้ามาเปิดเพลงที่คุณขอให้คุณฟังค่ะ!", inline=False)
        embed.add_field(name="n.stop", value="บอทจะปิดเพลง และออกจากห้องเสียงที่คุณอยู่ค่ะ", inline=False)
        embed.add_field(name="n.horo (คำถาม)", value="อยากถามอะไรถามมาได้เลยนะคะ ฉันจะทำนายให้คุณเองค่ะ!", inline=False)
        embed.add_field(name="n.time", value="อยากรู้เวลาตอนนี้หรอคะ? ใช้คำสั่งนี้ได้เลยค่ะ!", inline=False)
        embed.add_field(name="n.date", value="วันนี้วันที่เท่าไหร่น้า อยากรู้ก็ถามได้เลยนะคะ~", inline=False)
        embed.add_field(name="n.upic", value="ส่งรูปที่น่ารักๆของฉันให้คุณดูไงคะ~ (minato aqua)", inline=False)
        embed.add_field(name="n.ping", value="ตรวจสอบความหน่วงของตัวฉันเองค่ะ", inline=False)
        embed.add_field(name="n.help", value="ดูว่าตัวฉันสามารถทำอะไรได้บ้าง (ในตอนนี้)", inline=False)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('help plugin is ready.')
        
def setup(client):
    client.add_cog(help(client))