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
cartoon = ["https://www.youtube.com/watch?v=R2hA2LytWac", "https://www.youtube.com/watch?v=5TOq5Q-uZRI", "https://www.youtube.com/watch?v=mPTYJOW70k0", "https://www.youtube.com/watch?v=9ZBV5g1OJdI", "https://www.youtube.com/watch?v=ICAtmSeW_uY", "https://www.youtube.com/watch?v=X7uTyl8Jsso", "https://www.youtube.com/watch?v=Uvlo0ayA-wI", "https://www.youtube.com/watch?v=vaYlsIhPzwQ", "https://www.youtube.com/watch?v=3WWRYLNvJmA&"]
monke = ["https://www.youtube.com/watch?v=5s2E1zg2_9Q", "https://www.youtube.com/watch?v=ST0nEHwly_8", "https://www.youtube.com/watch?v=soxq9_TQ84U", "https://www.youtube.com/watch?v=yaNsK6h7e5A", "https://www.youtube.com/watch?v=bpvxmn5m8Sk", "https://www.youtube.com/watch?v=TADwhnnDMCw", "https://www.youtube.com/watch?v=bLpbt_Pm4Yc", "https://www.youtube.com/watch?v=rIPq9Fl5r44", "https://www.youtube.com/watch?v=DCmh5fvgqq4", "https://www.youtube.com/watch?v=QlPlZbb1qAw", "https://www.youtube.com/watch?v=sgjtqpUE91o", "https://www.youtube.com/watch?v=yfPJhWo8HR8"]

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
                    await self._channel.send(f'Tive um erro tentando processar sua música.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            msg = await self._channel.send(f'**Está tocando:** `{source.title}` pedido por '
                                               f'`{source.requester}`')
                                               
            
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

    def destroy(self, guild):
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Music(commands.Cog):

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
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Tive um erro tentando me conectar ao seu canal. '
                           'Por favor tenha certeza de que eu tenho permissões o suficiente para entrar no seu canal')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx):
        """Entra no mesmo canal que você."""
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            raise InvalidVoiceChannel('Nenhum canal para entrar.')

        player = self.get_player(ctx)
        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Movendo para o canal: <{channel}> tempo esgotado.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Movendo para o canal: <{channel}> tempo esgotado.')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='play', aliases=['sing'])
    async def play_(self, ctx, *, search: str):
        """Toca a música ou o vídeo desejado."""
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='pause')
    async def pause_(self, ctx):
        """Pausa a música."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send('Eu não estou tocando nada!')
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'**`{ctx.author}`**: Pausou a música!')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='resume')
    async def resume_(self, ctx):
        """Despausa a música."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou tocando nada!', )
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'**`{ctx.author}`**: Despausou a música!')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='skip')
    async def skip_(self, ctx):
        """Pula pra próxima música."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou tocando nada!')

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.send(f'**`{ctx.author}`**: Pulou a música!')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx):
        """Lista as músicas solicitadas."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou conectado a um canal de voz!')

        player = self.get_player(ctx)
        if player.queue.empty():
            return await ctx.send('Não tem mais músicas para tocar.')

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, 5))

        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(title=f'Próxima {len(upcoming)}', description=fmt)

        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        """Mostra o que está tocando no momento."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou conectado a um canal de voz!', )

        player = self.get_player(ctx)
        if not player.current:
            return await ctx.send('Eu não estou tocando nada!')

        player.np = await ctx.send(f'Tocando agora: `{vc.source.title}` '
                                   f'pedido por `{vc.source.requester}`', delete_after=5)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='volume', aliases=['vol'])
    async def change_volume(self, ctx, *, vol: float):
        """Coloca o volume do bot entre 1 e 100"""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou conectado a um canal de voz!', )

        if not 0 < vol < 101:
            return await ctx.send('Por favor, diga um valor entre 1 e 100.')

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        await ctx.send(f'**`{ctx.author}`**: Deixou o volume em **{vol}%**')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='stop', aliases=['leave'])
    async def stop_(self, ctx):
        """Para a música."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('Eu não estou tocando nada!')

        await self.cleanup(ctx.guild)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='cartoon', aliases=['funnysound'])
    async def cartoon_(self, ctx):
        """Toca algum som aleatório de cartoon antigo."""
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, random.choice(cartoon), loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name='monke', aliases=['monkey'])
    async def monke_(self, ctx):
        """uh uh ah ah"""

        await ctx.message.delete()
        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        source = await YTDLSource.create_source(ctx, random.choice(monke), loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def arriba(self, ctx):
        '''¡¡BAILA CONMIGO MONO!!'''
        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)
        source = await YTDLSource.create_source(ctx, random.choice(MARIACHI), loop=self.bot.loop, download=False)

        arriba = await player.queue.put(source)

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

def setup(client):
    client.add_cog(Music(client))
