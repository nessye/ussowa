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

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    a = ["https://tenor.com/view/a-dancing-dancing-a-pesing-gif-18704788"]
    b = ["https://tenor.com/view/letter-b-dancing-gif-9063746"]
    c = ["https://tenor.com/view/letter-c-dancing-gif-9063747"]

    alf = {}
    char_list = 'a'
    alt_char_list = "{https://tenor.com/view/a-dancing-dancing-a-pesing-gif-18704788}"
    for idx, char in enumerate(char_list):
        alf[char] = alt_char_list[idx]
        alf[alt_char_list[idx]] = char
    
    @commands.command(pass_context=True)
    async def abc(self, ctx, *, msg):
        """Ｖａｐｏｒｗａｖｅ."""
        result = ""
        for char in msg:
            if char in self.alf:
                result += self.alf[char]
            else:
                result += char
        await ctx.send(content=result)  # slice reverses the string

def setup(bot):
    bot.add_cog(Misc(bot))