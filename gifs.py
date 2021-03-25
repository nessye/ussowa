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
from PIL import Image
from datetime import datetime
from discord.ext import commands
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                    ZeroOrMore,Forward,nums,alphas,oneOf)
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
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



class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def abraçar(self, ctx, user: discord.Member):
        '''Abrace alguém!!'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
            description = f"{ctx.author.mention} abraçou você!! 🥰 {user.mention}"
        )
        r = requests.get("https://nekos.life/api/v2/img/hug").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)
    
    @commands.command()
    async def beijar(self, ctx, user: discord.Member):
        '''Beije alguém!!'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
            description = f"{ctx.author.mention} beijou você!! 😘 {user.mention}­"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/kiss").json()
        embed.set_image(url=str(r['url'])) 
 
        await ctx.send(embed=embed)
    
    @commands.command()
    async def mimar(self, ctx, user: discord.Member): 
        '''Dê carinho à alguém!!'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
            description = f"{ctx.author.mention} fez carinho em você!! 😊 {user.mention}­"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/cuddle").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)

    @commands.command()
    async def estapear(self, ctx, user: discord.Member):
        '''Dê um tapa em alguém!!'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
            description = f"{ctx.author.mention} deu um tapa em você!! 😂 {user.mention}"
        )
        
        r = requests.get("https://nekos.life/api/v2/img/slap").json()
        embed.set_image(url=str(r['url'])) 

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))
