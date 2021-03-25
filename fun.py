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

elogios=["Lindo",
"Bonitão",
"Bonitona",
"Fofo",
"Fofa",
"Fofucho",
"Fofucha",
"Gostoso",
"Gostosa",
"Meu mundo",
"Meu universo",
"Especial",
"Importante",
"Amorzinho",
"Bobo",
"Bobão",
"Bobona",
"Fedido",
"Fedida",
"Fedidinho",
"Fedidinha",
"Amor da minha vida",
"Docinho",
"Putinha",
"CUTICUTICUTICUTICUTI",
"Gay",
"Boiola",
"Imperador Mestre Senhor Da Minha Buceta",
"Princesa do clitoris maneiro",
"Kurwa"]
moeda = ["Cara.", "Coroa."]
trashtalk = ["geleia de ameixa", "carbono", "noob saibot", "zé gotinha da petrobras", "sombra 3d", "mística versao homem", "tao preto que eh azul", "sabonete de mecânico", "manete de play2", "luto eterno", "molho shoyu", "albino ao contrario", "fim do slide", "picolé de pixe", "mousse de graxa", "batman", "noturno", "venom", "mercurio humano", "capa de biblia", "memory card (1mb)", "fim de incendio", "blackout", "coca zero", "suco de pneu", "tapete de oficina", "picolé de asfalto", "derrapada de carreta", "vela preta", "cabo usb", "molho ingles", "vitamina de petróleo", "genio da bula de café", "peito do pé do Pedro", "metade da Zebra", "avatar defumado", "carvão humano", "uub do dbz", "nescau o cereal radical", "impressao digital", "nevermore", "faixa de pedestre velha", "começo do tunel", "jabuticaba", "fita cassete", "chao de oficina", "ps3", "Sao Benedito", "apagao", "arvore queimada", "00:00", "crioulo", "munição de churrasqueira"]
daered = ["https://cdn.discordapp.com/attachments/822336101208817696/822613588693745674/unknown.png", "https://cdn.discordapp.com/attachments/822336101208817696/822613381163909130/sdsdsdsd.png", "https://media.discordapp.net/attachments/739569443662856325/811511046270746654/daer.png?width=206&height=255", "https://cdn.discordapp.com/attachments/822336101208817696/822607134550130698/daer.png", "https://cdn.discordapp.com/attachments/822336101208817696/822607136802209815/daered.png", "https://media.discordapp.net/attachments/822336101208817696/822607138659500032/dssdsd.png?width=206&height=255", "https://cdn.discordapp.com/attachments/822336101208817696/822607138299314226/ddzvtbi-74bd690a-0882-409f-bb54-a5bdb75b2763.png", "https://media.discordapp.net/attachments/822336101208817696/822607138642722867/daered.png?width=452&height=498", "https://cdn.discordapp.com/attachments/822336101208817696/822607140816027718/mexican_biker_magic.png", "https://cdn.discordapp.com/attachments/739569443662856325/814281479357857833/unknown.png", "https://cdn.discordapp.com/attachments/739569443662856325/814162421735751711/unknown.png", "https://cdn.discordapp.com/attachments/739569443662856325/814162237916446730/unknown.png"]
mason = ["https://media.discordapp.net/attachments/822336101208817696/822614143915917342/Z.png?width=151&height=151", "https://cdn.discordapp.com/attachments/822336101208817696/822614161775132723/2Q.png", "https://media.discordapp.net/attachments/822336101208817696/822614177314242571/images.png?width=165&height=92", "https://cdn.discordapp.com/attachments/822336101208817696/822614190161395742/images.png", "https://media.discordapp.net/attachments/822336101208817696/822614205747691540/images.png?width=123&height=123", "https://media.discordapp.net/attachments/822336101208817696/822614235186987018/images.png?width=113&height=201", "https://media.discordapp.net/attachments/822336101208817696/822614260516651028/images.png?width=165&height=92"]

class NumericStringParserForPython3(object):
    '''
    Most of this code comes from the fourFn.py pyparsing example
    '''
    def pushFirst(self, strg, loc, toks ):
        self.exprStack.append( toks[0] )
    def pushUMinus(self, strg, loc, toks ):
        if toks and toks[0]=='-':
            self.exprStack.append( 'unary -' )
    def __init__(self):
        """
        Please use any of the following symbols:
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        """
        point = Literal( "." )
        e     = CaselessLiteral( "E" )
        fnumber = Combine( Word( "+-"+nums, nums ) +
                        Optional( point + Optional( Word( nums ) ) ) +
                        Optional( e + Word( "+-"+nums, nums ) ) )
        ident = Word(alphas, alphas+nums+"_$")
        plus  = Literal( "+" )
        minus = Literal( "-" )
        mult  = Literal( "*" )
        div   = Literal( "/" )
        lpar  = Literal( "(" ).suppress()
        rpar  = Literal( ")" ).suppress()
        addop  = plus | minus
        multop = mult | div
        expop = Literal( "^" )
        pi    = CaselessLiteral( "PI" )
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                (pi|e|fnumber|ident+lpar+expr+rpar).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar+expr+rpar)
                ).setParseAction(self.pushUMinus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( self.pushFirst ) )
        term = factor + ZeroOrMore( ( multop + factor ).setParseAction( self.pushFirst ) )
        expr << term + ZeroOrMore( ( addop + term ).setParseAction( self.pushFirst ) )
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
        # expr <<  general_term
        self.bnf = expr
        # this will map operator symbols to their corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {
                "+" : operator.add,
                "-" : operator.sub,
                "*" : operator.mul,
                "/" : operator.truediv,
                "^" : operator.pow }
        self.fn  = {
                "sin" : math.sin,
                "cos" : math.cos,
                "tan" : math.tan,
                "abs" : abs,
                "trunc" : lambda a: int(a),
                "round" : round,
                "sgn" : lambda a: abs(a)>epsilon and cmp(a,0) or 0}
    def evaluateStack(self, s ):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack( s )
        if op in "+-*/^":
            op2 = self.evaluateStack( s )
            op1 = self.evaluateStack( s )
            return self.opn[op]( op1, op2 )
        elif op == "PI":
            return math.pi # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op]( self.evaluateStack( s ) )
        elif op[0].isalpha():
            return 0
        else:
            return float( op )
    def eval(self,num_string,parseAll=True):
        self.exprStack=[]
        results=self.bnf.parseString(num_string,parseAll)
        val=self.evaluateStack( self.exprStack[:] )
        return val

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.nsp=NumericStringParserForPython3()
        
    @commands.command()
    async def gif(self, ctx, *, tag):
        '''Pega um gif aleatório.'''
        g = safygiphy.Giphy()
        tag = tag.lower()
        with open('data/nsfw.json')as f:
            nsfwgif = json.load(f)
        if tag in nsfwgif:
            return await ctx.send('`Por favor, use os comandos de nsfw para ver coisas desse tipo.`', delete_after=5)
        gif = g.random(tag=tag)
        color = discord.Color.dark_red()
        em = discord.Embed(color=color)
        em.set_image(url=str(gif.get('data', {}).get('image_original_url')))
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
    
    text_flip = {}
    char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}"
    alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::-1]
    for idx, char in enumerate(char_list):
        text_flip[char] = alt_char_list[idx]
        text_flip[alt_char_list[idx]] = char

    @commands.command()
    async def virus(self, ctx, virus=None, *, user: discord.Member = None):
        '''
        Destrua completamente o dispositivo de alguém usando esse comando!
        '''
        virus = virus or 'discord'
        user = user or ctx.author.mention
        with open('data/virus.txt') as f:
            animation = f.read().splitlines()
        base = await ctx.send(animation[0])
        for line in animation[1:]:
            await base.edit(content=line.format(virus=virus, user=user))
            await asyncio.sleep(random.randint(1, 4))

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def show_color(self, ctx, *, color: discord.Colour):
        '''Digite uma cor e veja ela.'''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    @commands.command(description='This command might get you banned')
    async def annoy(self, ctx, member: discord.Member=None, number: int=5):
        """Se você for banido não venha chorar."""
        if number > 5:
            number = 5
        member = member or ctx.author
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        if member != None:
            for x in range(number):
                await ctx.channel.trigger_typing()
                await ctx.send(member.mention)
                await asyncio.sleep(8)
        else:
            return await ctx.send(f"{ctx.author.mention}, eu não sei usar comandos, por favor me ajude!!")
    
    @commands.command(aliases=['calc', 'maths'])
    async def calculate(self, ctx, *, formula=None):
        """Matemática."""
        
        person = ctx.message.author
        user = ctx.author.mention

        if formula == None:
            # How can it calculate an empty message? Reee!
            msg = f'\u200BUso: `{ctx.prefix}{ctx.invoked_with} [qualquer fórmula matemática]`'
            e = discord.Embed()
            e.color = discord.Color.dark_red()
            e.description = f'{msg}'
            await ctx.send(embed=e)
            return

        try:
            answer=self.nsp.eval(formula)
        except:
            # If there's a problem in the input, show examples
            msg = f'Você escreveu errado \nTente algum desses:'
            e = discord.Embed()
            e.color = discord.Color.dark_red()
            e.description = f'\u200B{msg}'
            e.add_field(name='multiplicação', value="`num` * `num`", inline=True)
            e.add_field(name='divisão', value="`num` / `num`", inline=True)
            e.add_field(name='adição', value="`num` + `num`", inline=True)
            e.add_field(name='sobra', value="`num` - `num`", inline=True)
            e.add_field(name='exponencial', value="`num` ^ `num`")
            e.add_field(name='inteiro', 
                        value="[`num` + `num` | `num` - `num`] `num` 0 `num`..`num` 9 `num` +")
            await ctx.send(embed=e, delete_after=60)
            return

        # Correct input prints correct answer
        e = discord.Embed()
        e.color = discord.Color.dark_red()
        e.add_field(name='Conta:', value=f'```{formula}```', inline=True)
        e.add_field(name='Resultado:', value=f'```{round(answer, 2)}```', inline=True)
        await ctx.send(embed=e)

    @commands.command(aliases=['yt', 'vid', 'video'])
    async def youtube(self, ctx, *, search):
        """Procura por vídeos no youtube."""
        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    
    wave = {}
    char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    alt_char_list = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    for idx, char in enumerate(char_list):
        wave[char] = alt_char_list[idx]
        wave[alt_char_list[idx]] = char
    
    @commands.command(pass_context=True)
    async def vaporwave(self, ctx, *, msg):
        """Ｖａｐｏｒｗａｖｅ."""
        result = ""
        for char in msg:
            if char in self.wave:
                result += self.wave[char]
            else:
                result += char
        await ctx.send(content=result)  # slice reverses the string
    
    @commands.command()
    async def elogio(self, ctx):  
        """Manda um elogio aleatório para você usar com sua webzinha. 🥰"""
        await ctx.send(f"{random.choice(elogios)}.")
    
    @commands.command(pass_context=True)
    async def textflip(self, ctx, *, msg):
        """Deixa um texto de ponta cabeça."""
        result = ""
        for char in msg:
            if char in self.text_flip:
                result += self.text_flip[char]
            else:
                result += char
        await ctx.send(content=result[::-1])

    @commands.command()
    async def trashtalk(self, ctx):
        """Manda um xingamento aleatório."""
        await ctx.send(f"{random.choice(trashtalk)}")
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def d20(self, ctx):
        """Roda um dado de 20 lados."""
        await ctx.send(f"{randint(0,20)}")

    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def d100(self, ctx):
        """Roda um dado de 100 lados."""
        await ctx.send(f"{randint(0,100)}")

    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def d50(self, ctx):
        """Roda um dado de 50 lados."""
        await ctx.send(f"{randint(0,50)}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def d10(self, ctx):
        """Roda um dado de 10 lados."""
        await ctx.send(f"{randint(0,10)}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def coinflip(self, ctx):
        """Cara ou coroa."""
        await ctx.send(f"{random.choice(moeda)}")
    
    @commands.command(aliases=['daer'])
    async def daered(self, ctx):
        '''Daered.'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
        )
        embed.set_image(url=f"{random.choice(daered)}") 

        await ctx.send(embed=embed)
    
    @commands.command(aliases=['mason'])
    async def masonfoxworth(self, ctx):
        '''masonfoxworth.'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
        )
        embed.set_image(url=f"{random.choice(mason)}") 

        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Misc(bot))
