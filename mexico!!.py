import discord
from discord.ext import commands

import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
from random import randint
import random 

MEXICO = "🌯🌯🌮🌮🇲🇽🇲🇽🥳¡¡¡QUE EMPIECE LA FIESTA, CABRONE!!! 🥳🇲🇽🇲🇽🌮🌮🌯🌯"
AYAYA = "AYAYAYA:heart_eyes: :flag_mx: :dancer: :man_dancing: ¡¡VAMOS A BAILAR, BAILAR, BAILAR!!:dancer: :man_dancing: :flag_mx: :heart_eyes: AYAYAYA"
NACHOS = ":burrito: :taco::avocado: :burrito: :taco: :flag_mx: :heart_eyes: ¡¡¡NACHOS CON GUACAMOLE!!!:heart_eyes: :flag_mx: :taco: :burrito::avocado: :taco: :burrito:"
LOMEXICO = "🥳🥳🥳 🇲🇽🇲🇽🇲🇽¡¡¡¡VIVA LO MEXICO AYAYAYA!!!!🇲🇽🇲🇽🇲🇽🥳🥳🥳"
MACAQUITO = ":burrito: :taco::dancer: :man_dancing: :monkey_face: :orangutan: :monkey: :flag_mx: :zany_face: ¡¡¡¡GIRA GIRA GIRA MACAQUITO!!!!:zany_face: :flag_mx: :monkey: :orangutan: :monkey_face: :dancer: :man_dancing: :taco: :burrito:"
BURRITOTACO = "BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACOBURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco: BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:BURRITO:burrito:TACO:taco:"
NOO = ":cry::flag_mx::sob::flag_mx::cry::flag_mx::sob::flag_mx::cry:¡¡¡¡¡NOOOOOOO LA FESTANCIA ESTÁ TERMINANDO CABRON!!!!!:cry::flag_mx::sob::flag_mx::cry::flag_mx::sob::flag_mx::cry:"
PLATO = ":partying_face::flag_mx::flag_mx::flag_mx::cowboy: :beers: :cocktail: ¡¡¡NUESTRO PLATO ESPECIAL, TEQUILA EN EL SOMBRERO!!!:cocktail: :beers: :cowboy: :flag_mx::flag_mx::flag_mx::partying_face:"
BORRACHO = ":flag_mx::flag_mx: :heart_eyes: :flag_mx::taco: :burrito: :zany_face::zany_face::zany_face:¡¡¡¡AYAYAY CABRONE ESTOY BORRACHO!!!!:zany_face::zany_face::zany_face::burrito: :taco: :flag_mx: :heart_eyes: :flag_mx::flag_mx:"
ESTUDO = ":partying_face: :partying_face: :flag_mx::flag_mx: :burrito: :taco: :zany_face: :burrito: :taco: :flag_mx: :flag_mx: :heart_eyes: :heart_eyes:  ¡¡¡¡¡ESO ES TODO POR HOY PERSONAL, GRACIAS POR FIESTEJAR CONMIGO!!!!!:heart_eyes: :heart_eyes: :flag_mx: :flag_mx: :taco: :burrito: :zany_face: :taco: :burrito: :flag_mx::flag_mx:  :partying_face: :partying_face:"
MARIACHI = ["https://www.youtube.com/watch?v=V5yTmVxRN2g"]

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)

class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""

class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


class MusicPlayer(commands.Cog):

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(MACAQUITO)
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(PLATO)
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                # We are no longer playing this song...
                await self.np.delete()
            except discord.HTTPException:
                pass

    def destroy(self, guild):
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Misc(commands.Cog):

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('Esse comando não pode ser usado em mensagens privadas.')
            except discord.HTTPException:
                pass

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    def conect_(self, ctx):
        """Entra no mesmo canal que você."""
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            raise InvalidVoiceChannel('Nenhum canal para entrar.')

        player = self.get_player(ctx)
        vc = ctx.voice_client

    @commands.command()
    async def arriba(self, ctx):
        '''¡¡BAILA CONMIGO MONO!!'''
        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.conect_)

        player = self.get_player(ctx)
        source = await YTDLSource.create_source(ctx, random.choice(MARIACHI), loop=self.bot.loop, download=True)

        await player.queue.put(source)

        await ctx.send(MEXICO) 
        await asyncio.sleep(2)
        await ctx.send(PLATO) 
        await asyncio.sleep(2)
        await ctx.send(NACHOS) 
        await asyncio.sleep(2)
        await ctx.send(AYAYA) 
        await asyncio.sleep(2)
        await ctx.send(LOMEXICO) 
        await asyncio.sleep(2)
        await ctx.send(MACAQUITO) 
        await asyncio.sleep(2)
        await ctx.send(BURRITOTACO) 
        await asyncio.sleep(2)
        await ctx.send(NACHOS) 
        await asyncio.sleep(2)
        await ctx.send(BORRACHO) 
        await asyncio.sleep(2)
        await ctx.send(MEXICO) 
        await asyncio.sleep(2)
        await ctx.send(MACAQUITO)
        await asyncio.sleep(2)
        await ctx.send(LOMEXICO) 
        await asyncio.sleep(2)
        await ctx.send(BURRITOTACO) 
        await asyncio.sleep(2)
        await ctx.send(PLATO) 
        await asyncio.sleep(2)
        await ctx.send(BORRACHO) 
        await asyncio.sleep(2)
        await ctx.send(MEXICO) 
        await asyncio.sleep(2)
        await ctx.send(AYAYA) 
        await asyncio.sleep(2)
        await ctx.send(BURRITOTACO) 
        await asyncio.sleep(2)
        await ctx.send(NACHOS) 
        await asyncio.sleep(2)
        await ctx.send(PLATO) 
        await asyncio.sleep(2)
        await ctx.send(LOMEXICO) 
        await asyncio.sleep(2)
        await ctx.send(BURRITOTACO) 
        await asyncio.sleep(2)
        await ctx.send(BORRACHO) 
        await asyncio.sleep(2)
        await ctx.send(AYAYA) 
        await asyncio.sleep(2)
        await ctx.send(MEXICO) 
        await asyncio.sleep(2)
        await ctx.send(NACHOS) 
        await asyncio.sleep(2)
        await ctx.send(LOMEXICO) 
        await asyncio.sleep(2)
        await ctx.send(BORRACHO) 
        await asyncio.sleep(2)
        await ctx.send(MACAQUITO) 
        await asyncio.sleep(2)
        await ctx.send(PLATO) 
        await asyncio.sleep(2)
        await ctx.send(NACHOS) 
        await asyncio.sleep(2)
        await ctx.send(BURRITOTACO) 
        await asyncio.sleep(2)
        await ctx.send(NOO) 
        await ctx.send(ESTUDO)

def setup(bot):
    bot.add_cog(Misc(bot))