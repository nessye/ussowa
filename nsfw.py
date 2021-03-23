import discord
from discord.ext import commands
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import io
import safygiphy
from ext import embedtobox
import random
import nsfw_dl
from nsfw_dl.bases import BaseSearchXML
from discord.utils import get
import urllib.parse, urllib.request, re

class Nsfw(commands.Cog):
    """Comandos nsfw!"""
    data_format = "bs4/html"
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        if not ctx.channel.is_nsfw():
            return False
        git = self.bot.get_cog('Git')
        if not await git.starred('kyb3r/selfbot.py'):
            return False
        return True

    @commands.command()
    async def xbooru(self, ctx):
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass
            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen(
                "http://xbooru.com/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            image = soup.find(id="image").get("src")
            last = str(image.split('?')
                       [-2]).replace('//', '/').replace(':/', '://')
            em = discord.Embed(colour=discord.Color.blue())
            em.description = f'[Link da imagem inteira*]({last})'
            em.set_image(url=last)
            em.set_footer(text='* clique no link por sua conta e risco!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                await ctx.send('Não posso mandar embeds aqui!')
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'xbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command(aliases=['gel'])
    async def gelbooru(self, ctx):
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("https://gelbooru.com/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="image").get("src")
            image = partial.replace('//', '/').replace(':/', '://')

            em = discord.Embed(colour=discord.Color.blue())
            em.description = f'[Link da imagem inteira*]({image})'
            em.set_image(url=image)
            em.set_footer(text='* clique no link por sua conta e risco!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                # em_list = await embedtobox.etb(em)
                # for page in em_list:
                #    await ctx.send(page)
                await ctx.send('Não posso mandar embeds aqui!')
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'gelbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command(aliases=['dbooru'])
    async def danbooru(self, ctx):
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("https://danbooru.donmai.us/posts/random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="image").get("src")
            image = partial.replace('//', '/').replace(':/', '://')

            em = discord.Embed(colour=discord.Color.blue())
            em.description = f'[Link da imagem inteira*]({image})'
            em.set_image(url=image)
            em.set_footer(text='* clique no link por sua conta e risco!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                # em_list = await embedtobox.etb(em)
                # for page in em_list:
                #    await ctx.send(page)
                await ctx.send('Não posso mandar embeds aqui!')
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'gelbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')   

    @commands.command(aliases=['ph'])
    async def pornhub(self, ctx, *, search):
        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'https://pt.pornhub.com/video/search?' + query_string)
        search_results = re.findall(r'viewkey=ph(.{13})',
                                    htm_content.read().decode())
        await ctx.send('https://pt.pornhub.com/view_video.php?viewkey=ph' + search_results[0])


def setup(bot):
    bot.add_cog(Nsfw(bot))
