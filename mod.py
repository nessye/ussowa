import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import random
import pip
import os
import io
import json


class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def format_mod_embed(self, ctx, user, success, method, duration = None, location=None):
        emb = discord.Embed(timestamp=ctx.message.created_at)
        emb.set_author(name=method.title(), icon_url=user.avatar_url)
        emb.color = discord.Color.blue()
        emb.set_footer(text=f'User ID: {user.id}')
        if success:
            if method == 'ban' or method == 'hackban':
                emb.description = f'{user} was just {method}ned.'
            elif method == 'unmute':
                emb.description = f'{user} was just {method}d.'
            elif method == 'mute':
                emb.description = f'{user} was just {method}d for {duration}.'
            elif method == 'channel-lockdown' or method == 'server-lockdown':
                emb.description = f'`{location.name}` está em quarentena agora!'
            else:
                emb.description = f'{user} was just {method}ed.'
        else:
            if method == 'lockdown' or 'channel-lockdown':
                emb.description = f"Você não tem permissões para {method} `{location.name}`."
            else:
                emb.description = f"Você não tem permissões para {method} {user.name}."
        
        with open('data/config.json') as f:
            config = json.load(f)
            modlog = os.environ.get('MODLOG') or config.get('MODLOG')
        if modlog is None:
            await ctx.send('­', delete_after=5)
        else:
            modlog = discord.utils.get(self.bot.get_all_channels(), id=int(modlog))
            if modlog is None:
                await ctx.send('­', delete_after=5)
            else:
                await modlog.send(embed=emb)
            
        return emb

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='Por favor, dê um motivo!'):
        '''Expulsa alguém do servidor.'''
        try:
            await ctx.guild.kick(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'kick')

        await ctx.send(embed=emb)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='Por favor, dê um motivo!'):
        '''Bane alguém do servidor.'''
        try:
            await ctx.guild.ban(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'ban')

        await ctx.send(embed=emb)

    @commands.command()
    async def clean(self, ctx, quantity: int):
        '''Limpa um número de mensagens suas.'''
        if quantity <= 15:
            total = quantity +1
            async for message in ctx.channel.history(limit=total):
                if message.author == ctx.author:
                    await message.delete()
                    await asyncio.sleep(3.0)
        else:
            async for message in ctx.channel.history(limit=6):
                if message.author == ctx.author:
                    await message.delete()
                    await asyncio.sleep(3.0)

    @commands.command()
    async def bans(self, ctx):
        '''Mostra uma lista de usuários banidos do servidor.'''
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send('Você não tem permissão para ver os bans.')

        em = discord.Embed(title=f'Lista de membros banidos ({len(bans)}):')
        em.description = ', '.join([str(b.user) for b in bans])
        em.color = discord.Color.blue()

        await ctx.send(embed=em)

    @commands.command()
    async def addrole(self, ctx, member: discord.Member, *, rolename: str):
        '''Adiciona um cargo em outra pessoa.'''
        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
        if not role:
            return await ctx.send('Esse cargo não existe.')
        try:
            await member.add_roles(role)
            await ctx.send(f'Adicionado: `{role.name}`')
        except:
            await ctx.send("Eu não tenho permissões para adicionar esse cargo.")


    @commands.command()
    async def removerole(self, ctx, member: discord.Member, *, rolename: str):
        '''Tira um cargo de outra pessoa.'''
        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
        if not role:
            return await ctx.send('Esse cargo não existe.')
        try:
            await member.remove_roles(role)
            await ctx.send(f'Removido: `{role.name}`')
        except:
            await ctx.send("Eu não tenho permissões para remover esse cargo.")

    @commands.command()
    async def hackban(self, ctx, userid, *, reason=None):
        '''Bane alguém que não está no servidor.'''
        try:
            userid = int(userid)
        except:
            await ctx.send('ID inválido')
        
        try:
            await ctx.guild.ban(discord.Object(userid), reason=reason)
        except:
            success = False
        else:
            success = True

        if success:
            async for entry in ctx.guild.audit_logs(limit=1, user=ctx.guild.me, action=discord.AuditLogAction.ban):
                emb = await self.format_mod_embed(ctx, entry.target, success, 'hackban')
        else:
            emb = await self.format_mod_embed(ctx, userid, success, 'hackban')
        await ctx.send(embed=emb)

    @commands.command()
    async def mute(self, ctx, member:discord.Member, duration, *, reason=None):
        '''Tira a permissão de alguém de falar, mandar mensagem por um tempo específico.'''
        unit = duration[-1]
        if unit == 's':
            time = int(duration[:-1])
            longunit = 'seconds'
        elif unit == 'm':
            time = int(duration[:-1]) * 60
            longunit = 'minutes'
        elif unit == 'h':
            time = int(duration[:-1]) * 60 * 60
            longunit = 'hours'
        else:
            await ctx.send('Unidade inválida! Use `s`, `m`, ou `h`.')
            return

        progress = await ctx.send('Mutando usuário!')
        try:
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)

            for channel in ctx.guild.voice_channels:
                await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'mute', f'{str(duration[:-1])} {longunit}')
        progress.delete()
        await ctx.send(embed=emb)
        await asyncio.sleep(time)
        try:
            for channel in ctx.guild.channels:
                await channel.set_permissions(member, overwrite=None, reason=reason)
        except:
            pass
        
    @commands.command()
    async def unmute(self, ctx, member:discord.Member, *, reason=None):
        '''Remove as modificações de canal para um membro especificado.'''
        progress = await ctx.send('Desmutando usuário!')
        try:
            for channel in ctx.message.guild.channels:
                await channel.set_permissions(member, overwrite=None, reason=reason)
        except:
            success = False
        else:
            success = True
            
        emb = await self.format_mod_embed(ctx, member, success, 'unmute')
        progress.delete()
        await ctx.send(embed=emb)

    @commands.group(invoke_without_command=True)
    async def lockdown(self, ctx):
        """Deixa o servidor ou o canal em quarentena."""
        pass

    @lockdown.command(aliases=['channel'],)
    async def chan(self, ctx, channel:discord.TextChannel = None, *, reason=None):
        if channel is None: channel = ctx.channel
        try:
            await channel.set_permissions(ctx.guild.default_role, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
        except:
            success = False
        else:
            success = True
        emb = await self.format_mod_embed(ctx, ctx.author, success, 'channel-lockdown', 0, channel)
        await ctx.send(embed=emb)
    
    @lockdown.command()
    async def server(self, ctx, server:discord.Guild = None, *, reason=None):
        if server is None: server = ctx.guild
        progress = await ctx.send(f'Trancando {server.name}')
        try:
            for channel in server.channels:
                await channel.set_permissions(ctx.guild.default_role, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
        except:
            success = False
        else:
            success = True
        emb = await self.format_mod_embed(ctx, ctx.author, success, 'server-lockdown', 0, server)
        progress.delete()
        await ctx.send(embed=emb)
    
    @commands.command(aliases=['ul'])
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def unlock(self, ctx, channel:discord.TextChannel = None, *, reason=None):
        """Desbloqueia um canal pra todo mundo"""
        if channel:
            if channel in ctx.guild.text_channels:
                perms = channel.overwrites_for(ctx.guild.default_role)
                perms.send_messages = True
                await channel.set_permissions(ctx.guild.default_role, overwrite=perms)

                e = discord.Embed(color=discord.Color.blue())
                e.set_author(name=f'Desbloqueado o canal #{ctx.channel}')
                await ctx.send(embed=e)
            else:
                await ctx.send(content="Não é possivel desbloquear o canal.")
        else:
            await ctx.send(content="Canal não encontrado.")


    @commands.command(aliases=['sb'])
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def softban(self, ctx, member : discord.Member, *, reason='Por favor, dê um motivo!'):
        """Dá softban em um membro (Explusa e apaga as mensagens)"""
        if member:
            try:
                await ctx.guild.ban(member, reason=reason)
                await ctx.guild.unban(member)
            except discord.Forbidden:
                await ctx.send(content="Não tenho permissões para banir esse usuário.", ttl=5)
            except discord.HTTPException:
                await ctx.send(content="Alguma coisa deu errado.", ttl=5)
            else:
                e = discord.Embed(color=discord.Color.blue())
                e.set_author(icon_url="https://cdn.discordapp.com/attachments/800414805487648808/822065245941530654/daer.png",
                             name="Soft Banned: " + str(member))
                await ctx.send(embed=e)

    @commands.command(aliases=['perms'])
    @commands.guild_only()
    async def permissions(self, ctx, member : discord.Member):
        """Mostra permissões de um membro."""
        if member:
            true = '\n'.join(name.replace('_', ' ').title() for name, value in ctx.channel.permissions_for(member) if value is True)
            false = '\n'.join(name.replace('_', ' ').title() for name, value in ctx.channel.permissions_for(member) if value is False)

            e = discord.Embed(title="Permissões", color=discord.Color.blue(), timestamp=datetime.datetime.now())
            e.set_author(name=member, icon_url=member.avatar_url)
            e.add_field(name="Permitido", value=true, inline=False)
            e.add_field(name="Negado", value=false, inline=False)

            await ctx.send(embed=e)

def setup(bot):
	bot.add_cog(Mod(bot))