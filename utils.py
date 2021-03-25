import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from mtranslate import translate
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import wikipedia
import aiohttp
import inspect
import asyncio
import urbanasync
import cr_py
import time
import re
import io
import os
import random
import json
import base64
import requests
import DiscordUtils
from random import randint
import random

scary = ["Gostei muito do cheiro da sua camiseta, ele me lembra a minha mãe em 1687.", "Achei seu cabelo muito bonito, os fios me lembram daquelas c̡̪͉o̢̘ͅr̜͍͢d̨͖͚a͔̘͜s͙͎͢ n̬̬͜o͇͕͢ m̢̗̯ę͓͖u͎̦͜ p̢̗̟ę͎͇s̰̙͢c͈͖͢o̧͔̞ç̲̜͜o̠̜͜.", "Seus olhos são muito bonitos. Você sabia que os olhos são a janela para a alma de alguém? M̷e̵l̴h̸o̶r̸ v҉o҈c҉ê̵ t̴o̵m̵a҉r̴ c̶u̸i̷d̴a̷d̶o̶ c̶o̸m̴ i̵s҉s̵o̵", "Ah, ouvi falar de você por aqui... Não posso te contar muito sobre isso, mas cuidado ao atravessar a̧̰͚q̡̩̱u̢̫̲ḙ̢͎l͍̰͢a̳͔͜ rua, algo pode d̢̤̥a̯̲͜r̢͎͓ m̧̳̘ụ̢̗i̢͈̙t̡̙̲ǫ͙̥ e̢̳̯r̢̯̟r͚̯͜a̭̭͜d̡͇ͅǫ͚̠.", "Hm, vou ser breve porque não gostei muito de você. Seu corpo abriga a reencarnação do ḩ̫̥o̡̳͔ṃ̧͕ḛ̜͢m̨̘̮ q̡̙̩u̢͙ͅȩ̘̦ m̡̞͎ę̯̪ c̲̱͢ǫ͇̞n̨̖͕d̡̪̰e̲̗͢ņ̥̠o̰̤͜ṵ̡͔ a̡͚̥o̢̝̫ s̬̥͜o̯̮͢f̰͔͢r̮̠͜i̦̞͢m̡͓̭e̡̫̲n̨̳̜ţ͍̬o̮̠͜.", "Aliás, eles estão te esperando aqui desse lado. Dizem estar ansiosos para b̦͢ͅŗ͈͇i̧̬̬n̡̜̣c͎̮͢a̢͚̣ŗ̩̞e̠̯͢m̨͓͚ c̡̦̠o̢̗̙m̧̠͎ v̱͉͢o̢͍͈c̢̤̯ę͔͎̂"]

color = discord.Color.dark_red()

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
        self._last_embed = None
        self._rtfm_cache = None
        self._last_google = None
        self._last_result = None

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
      about = discord.Embed(color=color).add_field(name="Sobre o bot", value=f"Oii {ctx.author.mention}. {random.choice(scary)}. Já vi você e as outras pessoas muitas vezes, mas acredito que a maioria não sabe de mim. Eu sou o Ussowa, e sou m̨̫̮ą̘͕i̠̙͢s̨̖͇ q̖͇͢u̡̝̤ę̟͇ u̢̲̜m̡̭͓ b̨̤̗o̥̣͜t̢͖̮ d̨̮ͅo̢̙ͅ Ḑ̣̘į͇͈s̭̟͜ç̟̲o̢̳͈ŗ̖͍d̨̜̪. \n Será um prazer descomunal te ajudar no que precisar, seja numa simples decisão de cara ou coroa, bailar con mexicanos, ou M҉A҈T̸A̵R̶ o seu dispositivo:hugging:.\n\n ***Use .help <utils, mod, info, music, misc, nsfw> para ver os comandos!*** \n")
      about.set_footer(text=f'Minha a͖̟͜l̢̘͚m̧̬̫a̪͜ͅ só į͈͖ņ͙̖c͚̭͢o̧͍̫r̢̲̥p̖͙͢o̧͕͉ŗ̥͈ǫ̣͕ų̲̙ uma forma tecnológica por causa do meu mestre searomi, que cuidou da parte de p̷̧̤r̸̨͓e҈̧͙̣n̸̜͢d̷̢͉ȩ̶͉r̷̡̙ m҉̥̲͢i̸̢̪n҈͚̖͢ḥ̶̡a̸̢̩s̴̥͜ e҈̡͚ntranha҉s espi҈r҈itu҉ai҉s҈ em meio aos comandos e a minha mentora AmasZnaumHEY, que me ajudou a me comunicar com vocês.')
      about.set_thumbnail(url="https://cdn.discordapp.com/attachments/800414805487648808/824481583230615592/ff.png")
      msg = await ctx.send(embed=about)
      
    @help.command()
    async def utils(self, ctx):
      utils = "charinfo: Mostra informação sobre um ou mais caracteres específicos \n calculate: Calcula uma expressão para você. \n wiki: Mostra os principais resultados de uma pesquisa no wikipedia. \n emoji: Mostra a imagem inteira de um emoji. \n emotes: Lista todos os emojis do servidor. \n translate: Traduz um texto. \n show_color: Mostra uma cor do discord.(Para programadores de python)"
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos úteis", value=utils)
      await ctx.send(embed=embed)
      
    
    @help.command()
    async def mod(self, ctx):
      mod = "addrole: Adiciona um cargo em outra pessoa. \n ban: Bane alguém do servidor. \n bans: Mostra uma lista de usuários banidos do servidor. \n clean: Limpa um número de mensagens suas. \n hackban: Bane alguém que não está no servidor. \n kick: Explusa alguém do servidor. \n lockdown: Tranca o chat para os outros usuários. \n mute: Tira a permissão de alguém de falar e mandar mensagem no chat por um tempo específico. \n permissions: Mostra permissões de um membro. \n removerole: Tira o cargo de um usuário. \n softban: Expulsa e apaga as mensagens de um usuário. \n unlock: Destranca o chat para todo mundo. \n unmute: Remove as modificações de canal para um membro específico."
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos de adminstrador", value=mod)
      await ctx.send(embed=embed)
      
    
    @help.command()
    async def info(self, ctx):
      info = "channelinfo: Mostra informações de um canal. \n channels: Lista todos os canais. \n roleinfo: Mostra informações de um cargo. \n serverinfo: Mostra informações do servidor. \n serverlogo: Mostra o ícone do servidor. \n useravatar: Manda o ícone de um usuário. \n userinfo: Mostra informações de um usuário."
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos de informação", value=info)
      await ctx.send(embed=embed)
      

    @help.command()
    async def music(self, ctx):
      music = "connect: Entra na sua call. \n play: Reproduz um vídeo do YouTube \n stop: Para a música. \n pause: Pausa a música. \n skip: Pula para a próxima música. \n queue: Lista todas as músicas solicitadas. \n now_playing: Mostra o que está tocando no momento. \n pause: Pausa a música. \n resume: Despausa a música. \n volume: Coloca o volume do bot entre 1 e 100. \n cartoon: Toca algum efeito sonoro de cartoon antigo. \n monkey: uh uh ah ah \n arriba: ¡¡BAILA CONMIGO MONO!!"
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos de música", value=music)
      await ctx.send(embed=embed)
      
    
    @help.command()
    async def misc(self, ctx):
      misc = "abraçar: Abrace alguém!! \n beijar: Beije alguém!! \n mimar: Dê carinho à alguém! \n estapear:  Dê um tapa em alguém! \n annoy: Pinga alguém 5 vezes \n coinflip: Cara ou coroa. \n d10: Roda um dado de 10 lados. \n d20: Roda um dado de 20 lados. \n d50: Roda um dado de 50 lados. \n d100: Roda um dado de 100 lados.\n elogio: Manda um elogio aleatório para você usar com sua webzinha. \:smiling_face_with_3_hearts: \n gif: Pega algum gif aleatório. \n textflip: Deixa um texto de ponta cabeça. \n trashtalk: Manda algum xingamento racista aleatório. \n vaporwave: Ｖａｐｏｒｗａｖｅ. \n virus: Destrua completamente o dispositivo de alguém usando esse comando. \n youtube: Procura por vídeos no YouTube."
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos diversos", value=misc)
      await ctx.send(embed=embed)
      

    @help.command()
    async def nsfw(self, ctx):
      nsfw = "anal: Manda uma imagem ou gif hentai de anal. \n feet: Manda uma imagem ou gif hentai de pézinhos. \n hentai: Manda uma imagem ou gif de hentai. \n lewd: Manda uma imagem ou gif lascivo. \n neko: Manda alguma imagem ou gif hentai de neko. \n pussy: Manda uma imagem ou gif hentai de (você sabe o que.). \n trap: Manda uma imagem ou gif hentai de uma trap. \n yuri:  Manda alguma imagem ou gif hentai de lésbicas. \n gelbooru: Manda uma imagem aleatória do gelbooru. \n danbooru: Pega uma imagem aleatória do danbooru. \n xbooru: Pega uma imagem aleatória do xbooru. \n pornhub: Procura um vídeo no pornhub."
      embed = discord.Embed(color=discord.Color.dark_red())
      embed.add_field(name="Comandos +18", value=nsfw)
      await ctx.send(embed=embed)
      
    
    """@commands.command()
    async def help(self, ctx):
      about = discord.Embed(color=color).add_field(name="Sobre o bot", value=f"Oii {ctx.author.mention}. {random.choice(scary)}. Já vi você e as outras pessoas muitas vezes, mas acredito que a maioria não sabe de mim. Eu sou o Ussowa, e sou m̨̫̮ą̘͕i̠̙͢s̨̖͇ q̖͇͢u̡̝̤ę̟͇ u̢̲̜m̡̭͓ b̨̤̗o̥̣͜t̢͖̮ d̨̮ͅo̢̙ͅ Ḑ̣̘į͇͈s̭̟͜ç̟̲o̢̳͈ŗ̖͍d̨̜̪. \n Será um prazer descomunal te ajudar no que precisar, seja numa simples decisão de cara ou coroa, bailar con mexicanos, ou M҉A҈T̸A̵R̶ o seu dispositivo:hugging:.")
      about.set_footer(text=f'Minha a͖̟͜l̢̘͚m̧̬̫a̪͜ͅ só į͈͖ņ͙̖c͚̭͢o̧͍̫r̢̲̥p̖͙͢o̧͕͉ŗ̥͈ǫ̣͕ų̲̙ uma forma tecnológica por causa do meu mestre searomi, que cuidou da parte de p̷̧̤r̸̨͓e҈̧͙̣n̸̜͢d̷̢͉ȩ̶͉r̷̡̙ m҉̥̲͢i̸̢̪n҈͚̖͢ḥ̶̡a̸̢̩s̴̥͜ e҈̡͚ntranha҉s espi҈r҈itu҉ai҉s҈ em meio aos comandos e a minha mentora AmasZnaumHEY, que me ajudou a me comunicar com vocês.')
      await ctx.send(embed=about)"""

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        '''Mostra informação sobre um ou mais caracteres específicos.'''
        if len(characters) > 15:
            return await ctx.send('Muitos caracteres ({}/15)'.format(len(characters)))

        fmt = '`{1}` - `{2}` - <http://www.fileformat.info/info/unicode/char/{0}>'

        def to_string(c):
            digit = format(ord(c), 'x')
            name = unicodedata.name(c, 'Não foi encontrado nada com esse nome.')
            return fmt.format(digit, name, c)

        await ctx.send('\n'.join(map(to_string, characters)))

    @commands.command(pass_context=True)
    async def wiki(self, ctx, *, search: str = None):
        '''Mostra os principais resultados da wikipedia.'''
        if search == None:
            await ctx.channel.send(f'Usage: `{ctx.prefix}wiki [search terms]`')
            return

        results = wikipedia.search(search)
        if not len(results):
            no_results = await ctx.channel.send("Desculpe, não consegui achar nada.")
            await asyncio.sleep(5)
            await ctx.message.delete(no_results)
            return

        newSearch = results[0]
        try:
            wik = wikipedia.page(newSearch)
        except wikipedia.DisambiguationError:
            more_details = await ctx.channel.send('Por favor, dê mais detalhes.')
            await asyncio.sleep(5)
            await ctx.message.delete(more_details)
            return

        emb = discord.Embed()
        emb.color = color=discord.Color.dark_red()
        emb.title = wik.title
        emb.url = wik.url
        textList = textwrap.wrap(wik.content, 500, break_long_words=True, replace_whitespace=False)
        emb.add_field(name="Resultados da wikipedia", value=textList[0] + "...")
        await ctx.send(embed=emb)

    async def to_embed(self, ctx, params):
        '''Actually formats the parsed parameters into an Embed'''
        em = discord.Embed()

        if not params.count('{'):
            if not params.count('}'):
                em.description = params

        for field in self.get_parts(params):
            data = self.parse_field(field)

            color = data.get('color') or data.get('colour')
            if color == 'random':
                em.color = random.randint(0, 0xFFFFFF)
            elif color == 'chosen':
                maybe_col = os.environ.get('COLOR')
                if maybe_col:
                    raw = int(maybe_col.strip('#'), 16)
                    return discord.Color(value=raw)
                else:
                    return await ctx.send('A cor escolhida não existe.')

            elif color:
                color = int(color.strip('#'), 16)
                em.color = discord.Color(color)

            if data.get('description'):
                em.description = data['description']

            if data.get('desc'):
                em.description = data['desc']

            if data.get('title'):
                em.title = data['title']

            if data.get('url'):
                em.url = data['url']

            author = data.get('author')
            icon, url = data.get('icon'), data.get('url')

            if author:
                em._author = {'name': author}
                if icon:
                    em._author['icon_url'] = icon
                if url:
                    em._author['url'] = url

            field, value = data.get('field'), data.get('value')
            inline = False if str(data.get('inline')).lower() == 'false' else True
            if field and value:
                em.add_field(name=field, value=value, inline=inline)

            if data.get('thumbnail'):
                em._thumbnail = {'url': data['thumbnail']}

            if data.get('image'):
                em._image = {'url': data['image']}

            if data.get('footer'):
                em._footer = {'text': data.get('footer')}
                if data.get('icon'):
                    em._footer['icon_url'] = data.get('icon')

            if 'timestamp' in data.keys() and len(data.keys()) == 1:
                em.timestamp = ctx.message.created_at

        return em

    def get_parts(self, string):
        '''
        Splits the sections of the embed command
        '''
        for i, char in enumerate(string):
            if char == "{":
                ret = ""
                while char != "}":
                    i += 1
                    char = string[i]
                    ret += char
                yield ret.rstrip('}')

    def parse_field(self, string):
        '''
        Recursive function to get all the key val
        pairs in each section of the parsed embed command
        '''
        ret = {}

        parts = string.split(':')
        key = parts[0].strip().lower()
        val = ':'.join(parts[1:]).strip()

        ret[key] = val

        if '|' in string:
            string = string.split('|')
            for part in string:
                ret.update(self.parse_field(part))
        return ret

    async def build_rtfm_lookup_table(self):
        cache = {}

        page_types = {
            'rewrite': (
                'http://discordpy.rtfd.io/en/rewrite/api.html',
                'http://discordpy.rtfd.io/en/rewrite/ext/commands/api.html'
            )
        }

        for key, pages in page_types.items():
            sub = cache[key] = {}
            for page in pages:
                async with self.bot.session.get(page) as resp:
                    if resp.status != 200:
                        raise RuntimeError('Cannot build rtfm lookup table, try again later.')

                    text = await resp.text(encoding='utf-8')
                    root = etree.fromstring(text, etree.HTMLParser())
                    if root is not None:
                        nodes = root.findall(".//dt/a[@class='headerlink']")
                        for node in nodes:
                            href = node.get('href', '')
                            as_key = href.replace('#discord.', '').replace('ext.commands.', '')
                            sub[as_key] = page + href

        self._rtfm_cache = cache

    async def do_rtfm(self, ctx, key, obj):
        base_url = 'http://discordpy.rtfd.io/en/{}/'.format(key)

        if obj is None:
            await ctx.send(base_url)
            return

        if not self._rtfm_cache:
            await ctx.trigger_typing()
            await self.build_rtfm_lookup_table()

        # identifiers don't have spaces
        obj = obj.replace(' ', '_')

        if key == 'rewrite':
            pit_of_success_helpers = {
                'vc': 'VoiceClient',
                'msg': 'Message',
                'color': 'Colour',
                'perm': 'Permissions',
                'channel': 'TextChannel',
                'chan': 'TextChannel',
            }

            # point the abc.Messageable types properly:
            q = obj.lower()
            for name in dir(discord.abc.Messageable):
                if name[0] == '_':
                    continue
                if q == name:
                    obj = 'abc.Messageable.{}'.format(name)
                    break

            def replace(o):
                return pit_of_success_helpers.get(o.group(0), '')

            pattern = re.compile('|'.join(r'\b{}\b'.format(k)
                                          for k in pit_of_success_helpers.keys()))
            obj = pattern.sub(replace, obj)

        cache = self._rtfm_cache[key]
        matches = fuzzy.extract_or_exact(
            obj, cache, scorer=fuzzy.token_sort_ratio, limit=5, score_cutoff=50)

        e = discord.Embed(colour=discord.Colour.blurple())
        if len(matches) == 0:
            return await ctx.send('Could not find anything. Sorry.')

        e.description = '\n'.join('[{}]({}) ({}%)'.format(key, url, p) for key, p, url in matches)
        await ctx.send(embed=e)

    def parse_google_card(self, node):
        e = discord.Embed(colour=discord.Colour.blurple())

        # check if it's a calculator card:
        calculator = node.find(".//span[@class='cwclet']")
        if calculator is not None:
            e.title = 'Calculator'
            result = node.find(".//span[@class='cwcot']")
            if result is not None:
                result = ' '.join((calculator.text, result.text.strip()))
            else:
                result = calculator.text + ' ???'
            e.description = result
            return e

        # check for unit conversion card

        unit_conversions = node.xpath(".//input[contains(@class, '_eif') and @value]")
        if len(unit_conversions) == 2:
            e.title = 'Unit Conversion'

            # the <input> contains our values, first value = second value essentially.
            # these <input> also have siblings with <select> and <option selected=1>
            # that denote what units we're using

            # We will get 2 <option selected="1"> nodes by traversing the parent
            # The first unit being converted (e.g. Miles)
            # The second unit being converted (e.g. Feet)

            xpath = etree.XPath("parent::div/select/option[@selected='1']/text()")
            try:
                first_node = unit_conversions[0]
                first_unit = xpath(first_node)[0]
                first_value = float(first_node.get('value'))
                second_node = unit_conversions[1]
                second_unit = xpath(second_node)[0]
                second_value = float(second_node.get('value'))
                e.description = ' '.join(
                    (str(first_value), first_unit, '=', str(second_value), second_unit))
            except Exception:
                return None
            else:
                return e

        # check for currency conversion card
        if 'currency' in node.get('class', ''):
            currency_selectors = node.xpath(".//div[@class='ccw_unit_selector_cnt']")
            if len(currency_selectors) == 2:
                e.title = 'Currency Conversion'
                # Inside this <div> is a <select> with <option selected="1"> nodes
                # just like the unit conversion card.

                first_node = currency_selectors[0]
                first_currency = first_node.find("./select/option[@selected='1']")

                second_node = currency_selectors[1]
                second_currency = second_node.find("./select/option[@selected='1']")

                # The parent of the nodes have a <input class='vk_gy vk_sh ccw_data' value=...>
                xpath = etree.XPath("parent::td/parent::tr/td/input[@class='vk_gy vk_sh ccw_data']")
                try:
                    first_value = float(xpath(first_node)[0].get('value'))
                    second_value = float(xpath(second_node)[0].get('value'))

                    values = (
                        str(first_value),
                        first_currency.text,
                        f'({first_currency.get("value")})',
                        '=',
                        str(second_value),
                        second_currency.text,
                        f'({second_currency.get("value")})'
                    )
                    e.description = ' '.join(values)
                except Exception:
                    return None
                else:
                    return e

        # check for generic information card
        info = node.find(".//div[@class='_f2g']")
        if info is not None:
            try:
                e.title = ''.join(info.itertext()).strip()
                actual_information = info.xpath(
                    "parent::div/parent::div//div[@class='_XWk' or contains(@class, 'kpd-ans')]")[0]
                e.description = ''.join(actual_information.itertext()).strip()
            except Exception:
                return None
            else:
                return e

        # check for translation card
        translation = node.find(".//div[@id='tw-ob']")
        if translation is not None:
            src_text = translation.find(".//pre[@id='tw-source-text']/span")
            src_lang = translation.find(".//select[@id='tw-sl']/option[@selected='1']")

            dest_text = translation.find(".//pre[@id='tw-target-text']/span")
            dest_lang = translation.find(".//select[@id='tw-tl']/option[@selected='1']")

            # TODO: bilingual dictionary nonsense?

            e.title = 'Translation'
            try:
                e.add_field(name=src_lang.text, value=src_text.text, inline=True)
                e.add_field(name=dest_lang.text, value=dest_text.text, inline=True)
            except Exception:
                return None
            else:
                return e

        # check for "time in" card
        time = node.find("./div[@class='vk_bk vk_ans']")
        if time is not None:
            date = node.find("./div[@class='vk_gy vk_sh']")
            try:
                e.title = node.find('span').text
                e.description = f'{time.text}\n{"".join(date.itertext()).strip()}'
            except Exception:
                return None
            else:
                return e

        # time in has an alternative form without spans
        time = node.find("./div/div[@class='vk_bk vk_ans _nEd']")
        if time is not None:
            converted = "".join(time.itertext()).strip()
            try:
                # remove the in-between text
                parent = time.getparent()
                parent.remove(time)
                original = "".join(parent.itertext()).strip()
                e.title = 'Time Conversion'
                e.description = f'{original}...\n{converted}'
            except Exception:
                return None
            else:
                return e

        # check for definition card
        words = node.xpath(".//span[@data-dobid='hdw']")
        if words:
            lex = etree.XPath(".//div[@class='lr_dct_sf_h']/i/span")

            # this one is derived if we were based on the position from lex
            xpath = etree.XPath("../../../ol[@class='lr_dct_sf_sens']//"
                                "div[not(@class and @class='lr_dct_sf_subsen')]/"
                                "div[@class='_Jig']/div[@data-dobid='dfn']/span")
            for word in words:
                # we must go two parents up to get the root node
                root = word.getparent().getparent()

                pronunciation = root.find(".//span[@class='lr_dct_ph']/span")
                if pronunciation is None:
                    continue

                lexical_category = lex(root)
                definitions = xpath(root)

                for category in lexical_category:
                    definitions = xpath(category)
                    try:
                        descrip = [f'*{category.text}*']
                        for index, value in enumerate(definitions, 1):
                            descrip.append(f'{index}. {value.text}')

                        e.add_field(name=f'{word.text} /{pronunciation.text}/',
                                    value='\n'.join(descrip))
                    except:
                        continue

            return e

        # check for weather card
        location = node.find("./div[@id='wob_loc']")
        if location is None:
            return None

        # these units should be metric

        date = node.find("./div[@id='wob_dts']")

        # <img alt="category here" src="cool image">
        category = node.find(".//img[@id='wob_tci']")

        xpath = etree.XPath(
            ".//div[@id='wob_d']//div[contains(@class, 'vk_bk')]//span[@class='wob_t']")
        temperatures = xpath(node)

        misc_info_node = node.find(".//div[@class='vk_gy vk_sh wob-dtl']")

        if misc_info_node is None:
            return None

        precipitation = misc_info_node.find("./div/span[@id='wob_pp']")
        humidity = misc_info_node.find("./div/span[@id='wob_hm']")
        wind = misc_info_node.find("./div/span/span[@id='wob_tws']")

        try:
            e.title = 'Weather for ' + location.text.strip()
            e.description = f'*{category.get("alt")}*'
            e.set_thumbnail(url='https:' + category.get('src'))

            if len(temperatures) == 4:
                first_unit = temperatures[0].text + temperatures[2].text
                second_unit = temperatures[1].text + temperatures[3].text
                units = f'{first_unit} | {second_unit}'
            else:
                units = 'Unknown'

            e.add_field(name='Temperature', value=units, inline=False)

            if precipitation is not None:
                e.add_field(name='Precipitation', value=precipitation.text)

            if humidity is not None:
                e.add_field(name='Humidity', value=humidity.text)

            if wind is not None:
                e.add_field(name='Wind', value=wind.text)
        except:
            return None

        return e

    async def get_google_entries(self, query):
        url = f'https://www.google.com/search?q={uriquote(query)}'
        params = {
            'safe': 'on',
            'lr': 'lang_en',
            'hl': 'en'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/53.0'
        }

        # list of URLs and title tuples
        entries = []

        # the result of a google card, an embed
        card = None

        async with self.bot.session.get(url, params=params, headers=headers) as resp:
            if resp.status != 200:
                log.info('Google failed to respond with %s status code.', resp.status)
                raise RuntimeError('Google has failed to respond.')

            root = etree.fromstring(await resp.text(), etree.HTMLParser())

            # for bad in root.xpath('//style'):
            #     bad.getparent().remove(bad)

            # for bad in root.xpath('//script'):
            #     bad.getparent().remove(bad)

            # with open('google.html', 'w', encoding='utf-8') as f:
            #     f.write(etree.tostring(root, pretty_print=True).decode('utf-8'))

            """
            Tree looks like this.. sort of..
            <div class="rc">
                <h3 class="r">
                    <a href="url here">title here</a>
                </h3>
            </div>
            """

            card_node = root.xpath(".//div[@id='rso']/div[@class='_NId']//"
                                   "div[contains(@class, 'vk_c') or @class='g mnr-c g-blk' or @class='kp-blk']")

            if card_node is None or len(card_node) == 0:
                card = None
            else:
                card = self.parse_google_card(card_node[0])

            search_results = root.findall(".//div[@class='rc']")
            # print(len(search_results))
            for node in search_results:
                link = node.find("./h3[@class='r']/a")
                if link is not None:
                    # print(etree.tostring(link, pretty_print=True).decode())
                    entries.append((link.get('href'), link.text))

        return card, entries

    @commands.command()
    async def avatar(sself, ctx): 
        """Manda algum avatar de anime aleatório."""
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/avatar").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))
    
    @commands.command()
    async def wallpaper(sself, ctx): 
        """Manda algum wallpaper de anime aleatório."""
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
        em = discord.Embed(description=f'', color=color)
        em.set_image(url=str(r['url']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))
    
    
    @commands.command()
    async def emoji(sself, ctx, emoji : discord.PartialEmoji):
      await ctx.send(emoji.url)
    
    @commands.command(aliases=['trans'])
    async def translate(self, ctx, lang, *, text):
        """Traduz um texto!"""
        conv = self.lang_conv
        if lang in conv:
            return await ctx.send(f'**{translate(text, lang)}**')
        lang = dict(zip(conv.values(), conv.keys())).get(lang.lower().title())
        if lang:
            await ctx.send(f'*{translate(text, lang)}*')
        else:
            await ctx.send('`Língua não disponivel.`', delete_after=5)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

def setup(bot: commands.Bot):
    bot.add_cog(Utils(bot))
