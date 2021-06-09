import discord
import os
import random
from discord.ext import commands 
from os.path import join, dirname
from dotenv import load_dotenv

import json

with open('../bot/botconfig.json') as config_file:
    data = json.load(config_file)

token = data['token']
prefix = data['prefix']
version = data['version']
adminid = data['adminid']
adminuser = data['adminuser']

#==================================================

class horoscope(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def horo(self,ctx, *, question):
        responses = ["แน่นอนอยู่แล้วค่า",
                    "ก็น่าจะเป็นอย่างนั้นนะคะ",
                    "โดยไม่มีข้อกังขาเลยค่ะ!",
                    "ใช่แน่นอนค่าา",
                    "คุณอาจพึ่งพามันได้นะคะ",
                    "เท่าที่เค้าเห็น เค้าว่าใช่น้า",
                    "เป็นไปได้สุดๆเลยค่าา",
                    "ก็ดูท่าจะดีนะคะ",
                    "ใช่ค่า",
                    "เลือกทางที่คุณอยากดีกว่านะคะ",
                    "อะไรนะคะไม่เข้าใจ ขออีกรอบได้ไหมคะ?",
                    "ไว้มาถามใหม่ทีหลังนะคะ..",
                    "คุณไม่ควรรู้ตอนนี้จะดีกว่านะคะ..555",
                    "อันนี้ฉันไม่รู้จริงๆค่ะ",
                    "เรียบเรียงคำพูดดีๆ แล้วขออีกรอบได้ไหมคะะ",
                    "อย่าไปนับมันเลยค่ะ",
                    "ฉันคิดว่าไม่นะคะ",
                    "หัวใจของฉัน..มันบอกว่าไม่ค่ะ",
                    "ดูท่าไม่ค่อยจะดีเลยนะคะ",
                    "แย่มากเลยค่ะ.."]
        embed=discord.Embed(title=" ", description=('คำถามจาก : ' + format(ctx.message.author.mention)), color=0x00ffff)
        embed.set_author(name="nicenathapong bot Future horoscope", icon_url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706978463814516809/846225082375340042/minato_aqua_lite.png")
        embed.add_field(name="ถามว่า :", value=(question), inline=False)
        embed.add_field(name="คำตอบ :", value=(random.choice(responses)), inline=False)
        embed.set_footer(text=("bot by nicenathapong | " + (version) + " | run on .python"))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('horoscope plugin is ready.')

def setup(client):
    client.add_cog(horoscope(client))