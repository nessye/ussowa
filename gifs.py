from __future__ import division
import discord
import math
import operator
import colorthief
import asyncio
import random
import emoji
import copy
import io
import aiohttp
import json
import os
import requests
import urllib.parse, urllib.request, re
import urbanasync
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sympy import solve
from PIL import Image
from datetime import datetime
from discord.ext import commands
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                    ZeroOrMore,Forward,nums,alphas,oneOf)
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
from sympy import solve
from PIL import Image
import safygiphy
from ext import embedtobox
from random import randint
import random 
import aiohttp
import discord
import json
import logging
import mimetypes
import random
import re
from discord.ext import commands
from random import choice

abraço = ["https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846", "https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856", "https://media1.tenor.com/images/4e9c3a6736d667bea00300721cff45ec/tenor.gif?itemid=14539121", "https://media1.tenor.com/images/5ccc34d0e6f1dccba5b1c13f8539db77/tenor.gif?itemid=17694740", "https://media1.tenor.com/images/78d3f21a608a4ff0c8a09ec12ffe763d/tenor.gif?itemid=16509980", "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788", "https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498", "https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705", "https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587", "https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978", "https://media1.tenor.com/images/ee3c3831a62667dc84ec4149a1651d8b/tenor.gif?itemid=14924015", "https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885", "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075", "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500", "https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480", "https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774", "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935"]
beijo = ["https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544", "https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722", "https://media1.tenor.com/images/626cb1e13142bce7f228ab8e30e2519c/tenor.gif?itemid=16896135", "https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515", "https://media1.tenor.com/images/3d56f6ef81e5c01241ff17c364b72529/tenor.gif?itemid=13843260", "https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422", "https://media1.tenor.com/images/d307db89f181813e0d05937b5feb4254/tenor.gif?itemid=16371489", "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865", "https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/tenor.gif?itemid=12837192", "https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409", "https://media1.tenor.com/images/230e9fd40cd15e3f27fc891bac04248e/tenor.gif?itemid=14751754", "https://media1.tenor.com/images/e76e640bbbd4161345f551bb42e6eb13/tenor.gif?itemid=4829336", "https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850", "https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif?itemid=5649376", "https://media1.tenor.com/images/ef4a0bcb6e42189dc12ee55e0d479c54/tenor.gif?itemid=12143127", "https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif?itemid=6155670", "https://media1.tenor.com/images/621ceac89636fc46ecaf81824f9fee0e/tenor.gif?itemid=4958649"]
carinho = ["https://media1.tenor.com/images/d0c2e7382742f1faf8fcb44db268615f/tenor.gif?itemid=5853736", "https://media1.tenor.com/images/dba1b0c24bb8bf784bb28ea8ff035e3e/tenor.gif?itemid=10403234", "https://media1.tenor.com/images/6d73b0a9cadef5310be4b6160d2f959a/tenor.gif?itemid=12099823", "https://media1.tenor.com/images/69c4983081641e997a05a4f2e121d53a/tenor.gif?itemid=14891948", "https://media1.tenor.com/images/207a3d5d5fb5f7cc09b64a3643fd9125/tenor.gif?itemid=17265727", "https://media1.tenor.com/images/29bd2a0cf5d863c3c803b3f4ab8d31f5/tenor.gif?itemid=17236791", "https://media1.tenor.com/images/7edded2757934756fdc240019d956cb3/tenor.gif?itemid=16403937", "https://media1.tenor.com/images/62e62c1d2c5018313ac1067dfbc7562e/tenor.gif?itemid=15434284", "https://media1.tenor.com/images/5ccc34d0e6f1dccba5b1c13f8539db77/tenor.gif?itemid=17694740", "https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774", "https://media1.tenor.com/images/8f8ba3baeecdf28f3e0fa7d4ce1a8586/tenor.gif?itemid=12668750"]
tapa = ["https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612", "https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720", "https://media1.tenor.com/images/612e257ab87f30568a9449998d978a22/tenor.gif?itemid=16057834", "https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956", "https://media1.tenor.com/images/3fd96f4dcba48de453f2ab3acd657b53/tenor.gif?itemid=14358509", "https://media1.tenor.com/images/b7a844cc66ca1c6a4f06c266646d070f/tenor.gif?itemid=17423278", "https://media1.tenor.com/images/a9b8bd2060d76ec286ec8b4c61ec1f5a/tenor.gif?itemid=17784858", "https://media1.tenor.com/images/528ff731635b64037fab0ba6b76d8830/tenor.gif?itemid=17078255", "https://media1.tenor.com/images/53f7a45f41b45f46c9a6c4dc154e58c5/tenor.gif?itemid=16268549", "https://media1.tenor.com/images/37c72d1a4a4ad8108897642f7bebc4be/tenor.gif?itemid=17845941", "https://media1.tenor.com/images/6885c7676d8645bf2891138564159713/tenor.gif?itemid=4436362"]

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def abraçar(self, ctx, user: discord.Member):
        '''Abrace alguém!!'''
        embed = discord.Embed(
            color = discord.Color.blue(),
            title=f"{ctx.author} abraçou você!! 🥰 {user}­"
        )
        r = requests.get("https://nekos.life/api/v2/img/hug").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)
    
    @commands.command()
    async def beijar(self, ctx, user: discord.Member):
        '''Beije alguém!!'''
        embed = discord.Embed(
            color = discord.Color.blue(),
            title=f"{ctx.author} beijou você!! 😘 {user}­"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/kiss").json()
        embed.set_image(url=str(r['url'])) 
 
        await ctx.send(embed=embed)
    
    @commands.command()
    async def mimar(self, ctx, user: discord.Member):
        '''Dê carinho à alguém!!'''
        embed = discord.Embed(
            color = discord.Color.blue(),
            title=f"{ctx.author} fez carinho em você!! 😊 {user}­"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/cuddle").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)

    @commands.command()
    async def estapear(self, ctx, user: discord.Member):
        '''Dê um tapa em alguém!!'''
        embed = discord.Embed(
            color = discord.Color.blue(),
            title=f"{ctx.author} deu um tapa em você!! 😂 {user}­"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/slap").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))