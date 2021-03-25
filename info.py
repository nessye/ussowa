import discord
from discord.ext import commands
from urllib.parse import urlparse
from ext import embedtobox
import datetime
import asyncio
import psutil
import random
import pip
import json
import os
import io

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def channels(self, ctx, serverid:int = None):
        """Mostra todos os canais."""

        if serverid is None:
            server = ctx.guild
        else:
            server = discord.utils.get(self.bot.guilds, id=serverid)
            if server is None:
                return await ctx.send('Server não encontrado!')

        e = discord.Embed()
        e.color = discord.Color.dark_red()

        voice = ''
        text = ''
        categories = ''

        for channel in server.voice_channels:
            voice += f'\U0001f508 {channel}\n'
        for channel in server.categories:
            categories += f'\U0001f4da {channel}\n'
        for channel in server.text_channels:
            text += f'\U0001f4dd {channel}\n'
        
        if len(server.text_channels) > 0:
            e.add_field(name='Canais de texto', value=f'```{text}```')
        if len(server.categories) > 0:
            e.add_field(name='Categorias', value=f'```{categories}```')
        if len(server.voice_channels) > 0:
            e.add_field(name='Canais de voz', value=f'```{voice}```')

        try:
            await ctx.send(embed=e)
        except discord.HTTPException:
            em_list = await embedtobox.etb(e)
            for page in em_list:
                await ctx.send(page)
    
    @commands.command(aliases=["ri","role"], no_pm=True)
    @commands.guild_only()
    async def roleinfo(self, ctx, *, role: discord.Role):
        '''Mostra informações de um cargo específico.'''
        guild = ctx.guild

        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} dias atrás!)".format(role_created, since_created)
        members = ''
        i = 0
        for user in role.members:
            members += f'{user.name}, '
            i+=1
            if i > 30:
                break

        if str(role.colour):
            color = discord.Color.dark_red()
        else:
            color = discord.Color.dark_red()
            color = role.colour

        em = discord.Embed(color=color)
        em.set_author(name=role.name)
        em.add_field(name="Usuários", value=len(role.members))
        em.add_field(name="Mencionável", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Posição", value=role.position)
        em.add_field(name="Dirigido", value=role.managed)
        em.add_field(name="Cor", value=color)
        em.add_field(name='Data de criação', value=created_on)
        em.add_field(name='Membros', value=members[:-2], inline=False)
        em.set_footer(text=f'ID do cargo: {role.id}')
        await ctx.send(embed=em)
    
    @commands.command(aliases=['av'])
    async def useravatar(self, ctx, *, member : discord.Member=None):
        '''Manda o avatar de um usuário específico.'''
        member = member or ctx.author.mention
        av = str(member.avatar_url)
        if ".gif" in av:
            av += "&f=.gif"
        color = discord.Color.dark_red()
        em = discord.Embed(url=av, color=color)
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
            try:
                async with ctx.session.get(av) as resp:
                    image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, 'avatar.png'))
            except discord.HTTPException:
                await ctx.send(av)
    
    @commands.command(aliases=['servericon'], no_pm=True)
    async def serverlogo(self, ctx):
        '''Manda o ícone do servidor.'''
        icon = str(ctx.guild.icon_url)
        color = discord.Color.dark_red()
        server = ctx.guild
        em = discord.Embed(color=color, url=icon)
        em.set_author(name=server.name, icon_url=icon)
        em.set_image(url=icon)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
            try:
                async with ctx.session.get(icon) as resp:
                    image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, 'serverlogo.png'))
            except discord.HTTPException:
                await ctx.send(icon)

    @commands.command(aliases=['server', 'sinfo', 'si'], pass_context=True, invoke_without_command=True)
    async def serverinfo(self, ctx, *, msg=""):
        '''Mostra informações do servidor.'''
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        if ctx.invoked_subcommand is None:
            if msg:
                server = None
                try:
                    float(msg)
                    server = self.bot.get_guild(int(msg))
                    if not server:
                        return await ctx.send(
                                              self.bot.bot_prefix + 'Server não encontrado.')
                except:
                    for i in self.bot.guilds:
                        if i.name.lower() == msg.lower():
                            server = i
                            break
                    if not server:
                        return await ctx.send(self.bot.bot_prefix + 'Não foi possivel encontrar um servidor.')
            else:
                server = ctx.message.guild
        
        self.bot = ctx

        role_count = len(server.roles)
        emoji_count = len(server.emojis)
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(server.channels) - text_channels - voice_channels

        embed = discord.Embed(
            title="Informações do server",
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Nome", value=name)
        embed.add_field(name="Dono", value=ctx.guild.owner)
        embed.add_field(name="ID do server", value=id, inline=True)
        embed.add_field(name="Região", value=region, inline=True)
        embed.add_field(name="Quantidade de membros", value=memberCount, inline=True)
        embed.add_field(name="Quantidade de emojis", value=str(emoji_count))
        embed.add_field(name="Quantidade de cargos", value=str(role_count))
        embed.add_field(name="Criado em", value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed.add_field(name="Nivel de verificado", value=str(server.verification_level))
        embed.add_field(name="Canais de texto", value=text_channels)
        embed.add_field(name="Canais de voz", value=voice_channels)
        embed.add_field(name="Categorias", value=categories)
        embed.add_field(name="Cargos", value=len(server.roles))
        
        await ctx.send(embed=embed)
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def userinfo(self, ctx, user: discord.Member):
        '''Mostra informações de um usuário específico.'''
        embed = discord.Embed(
            color = discord.Color.dark_red(),
            title=f"{user}"
        )

        server = ctx.guild

        roles = []
        for role in user.roles:
            roles.append(role)

        embed.set_thumbnail(url=f"{user.avatar_url}") 
        embed.set_footer(text=f"Pedido por: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID:", value=user.id)
        embed.add_field(name="Nome no server:", value=user.display_name)
        embed.add_field(name="Criou a conta em:", value=user.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Entrou no server em:", value=user.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Cargos ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Cargo mais alto", value=user.top_role.mention)
        embed.add_field(name="Bot?", value=user.bot)

        await ctx.send(embed=embed)

    @commands.command(aliases=['channel', 'cinfo', 'ci'], pass_context=True, no_pm=True)
    async def channelinfo(self, ctx, *, channel: int = None):
        """Mostra informações de um canal específico."""
        if not channel:
            channel = ctx.message.channel
        else:
            channel = self.bot.get_channel(channel)
        data = discord.Embed()
        if hasattr(channel, 'mention'):
            data.description = "**Informação sobre o canal:** " + channel.mention
        if hasattr(channel, 'changed_roles'):
            if len(channel.changed_roles) > 0:
                data.color = discord.Colour.dark_red() if channel.changed_roles[0].permissions.read_messages else discord.Colour.red()
        if isinstance(channel, discord.TextChannel): 
            _type = "Texto"
        elif isinstance(channel, discord.VoiceChannel): 
            _type = "Voz"
        else: 
            _type = "Desconhecido"
        data.add_field(name="Tipo de canal", value=_type)
        data.add_field(name="ID", value=channel.id, inline=False)
        if hasattr(channel, 'position'):
            data.add_field(name="Posição", value=channel.position)
        if isinstance(channel, discord.VoiceChannel):
            if channel.user_limit != 0:
                data.add_field(name="Numero de usuários", value="{}/{}".format(len(channel.voice_members), channel.user_limit))
            else:
                data.add_field(name="Numero de usuários", value="{}".format(len(channel.voice_members)))
            userlist = [r.display_name for r in channel.members]
            if not userlist:
                userlist = "None"
            else:
                userlist = "\n".join(userlist)
            data.add_field(name="Usuários", value=userlist)
            data.add_field(name="Bitrate", value=channel.bitrate)
        elif isinstance(channel, discord.TextChannel):
            try:
                pins = await channel.pins()
                data.add_field(name="Mensagens fixadas", value=len(pins), inline=True)
            except discord.Forbidden:
                pass
            data.add_field(name="Membros", value="%s"%len(channel.members))
            if channel.topic:
                data.add_field(name="Tópico", value=channel.topic, inline=False)
            hidden = []
            allowed = []
            for role in channel.changed_roles:
                if role.permissions.read_messages is True:
                    if role.name != "@everyone":
                        allowed.append(role.mention)
                elif role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        hidden.append(role.mention)
            if len(allowed) > 0: 
                data.add_field(name='Cargos permitidos({})'.format(len(allowed)), value=', '.join(allowed), inline=False)
            if len(hidden) > 0:
                data.add_field(name='Cargos restritos({})'.format(len(hidden)), value=', '.join(hidden), inline=False)
        if channel.created_at:
            data.set_footer(text=("Criado há {} ({} dias atrás)".format(channel.created_at.strftime("%d %b %Y %H:%M"), (ctx.message.created_at - channel.created_at).days)))
        await ctx.send(embed=data)

    @commands.command(aliases=["e"])
    @commands.guild_only()
    async def emojis(self, ctx):
        """Mostra todos os emotes disponíveis no server."""
        unique_emojis = set(ctx.message.guild.emojis)
        em = discord.Embed(timestamp=datetime.datetime.now(), title='Emotes [%s]' % len(unique_emojis), colour=discord.Color.dark_red())
        if unique_emojis:
            fields = []
            field = ''
            for i, emote in enumerate(unique_emojis, 1):
                if (len(field + str(emote) + ' ')) <= 1024:
                    field += str(emote) + ' '
                    if i == len(unique_emojis):
                        fields.append(field)
                else:
                    fields.append(field)
                    field = str(emote) + ' '
            for i in fields:
                em.add_field(name='﻿', value=i, inline=False)
        else:
            em.add_field(name='Emotes', value='Não encontrado!', inline=False)
        await ctx.send(embed=em)
    
def setup(bot):
    bot.add_cog(Information(bot))
