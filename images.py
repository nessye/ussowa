from discord.ext import commands
import discord
import aiohttp

import config
from io import BytesIO
import random
import datetime
from mtranslate import translate
from googletrans import Translator


monika_faces = [x for x in "abcdefghijklmnopqr"]
natsuki_faces = [x for x in "abcdefghijklmnopqrstuvwxyz"]
natsuki_faces.extend(["1t", "2bt", "2bta", "2btb", "2btc", "2btd", "2bte", "2btf", "2btg", "2bth", "2bti",
                      "2t", "2ta", "2tb", "2tc", "2td", "2te", "2tf", "2tg", "2th", "2ti"])
sayori_faces = [x for x in "abcdefghijklmnopqrstuvwxy"]
yuri_faces = [x for x in "abcdefghijklmnopqrstuvwx"]
yuri_faces.extend(["y1", "y2", "y3", "y4", "y5", "y6", "y7"])
ddlc_items = {
    "body": {
        "monika": [ "1", "2" ],
        "natsuki": [ "1b", "1", "2b", "2"],
        "yuri": ["1b", "1", "2b", "2"],
        "sayori": ["1b", "1", "2b", "2"]
    },
    "face": {
        "monika": monika_faces,
        "natsuki": natsuki_faces,
        "yuri": yuri_faces,
        "sayori": sayori_faces
    }
}

ddlc_get_character = {
    "y": "yuri",
    "n": "natsuki",
    "m": "monika",
    "s": "sayori"
}

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.session.close()
        del self.session

    async def __get_image(self, ctx, user=None):
        if user:
            if user.is_avatar_animated():
                return str(user.avatar_url_as(format="gif"))
            else:
                return str(user.avatar_url_as(format="png"))

        await ctx.trigger_typing()

        message = ctx.message

        if len(message.attachments) > 0:
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            await ctx.send("Send me an image!")
            x = await self.bot.wait_for('message', check=check, timeout=15)
        except:
            return await ctx.send("Timed out...")

        if not len(x.attachments) >= 1:
            return await ctx.send("No images found.")

        return x.attachments[0].url

    def __embed_json(self, data, key="message"):
        em = discord.Embed(color=0xDEADBF)
        em.set_image(url=data[key])
        return em

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def animeface(self, ctx, user: discord.Member = None):
        """Detect anime faces in an image"""
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img

        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=animeface&image=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poop(self, ctx, user: discord.Member = None):
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        payload = {
            "Content": img,
            "Type": "CaptionRequest"
        }
        url = "https://captionbot.azurewebsites.net/api/messages"
        translator = Translator(to_lang='pt')
        try:
            async with self.session.post(url, headers=headers, json=payload) as r:
                data = await r.text()
            em = discord.Embed(color=discord.Color.dark_red(), title=str(translator.translate(data).replace('&quot;', '')))
            em.set_image(url=img)
            await ctx.send(embed=em)
        except:
            await ctx.send("Não foi possível processar a imagem.")
    
def setup(bot):
    bot.add_cog(Fun(bot))
