import discord
import asyncio
from discord.ext.commands import AutoShardedBot, when_mentioned_or
import os
from time import sleep
import datetime

modulos = ["utils", "info", "fun", "tictactoe", "nsfw2", "mod", "gifs", "mexico!!", "voice", "nsfw"]

client = AutoShardedBot(command_prefix=".", case_insensitive=True)

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(0)
screen_clear()

@client.event
async def on_ready():
    print(f"---------------------------------")
    print(f"{client.user.name} está online.")
    print(f"{datetime.datetime.now()}.")
    print(f"Feito por searomi#0246.")
    print(f"Logado como: {client.user}.")
    print(f"ID do usuário: {client.user.id}.")
    print(f"Versão 1.0.4.")
    print(f"---------------------------------")
    await client.wait_until_ready()
    await client.change_presence(status=discord.Status.online, afk=True)
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="os seus comandos, mestre!"))    
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="os seus movimentos, mestre."))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="roleta russa com sua família, mestre."))
        await asyncio.sleep(10)

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("ODIxNTgxMTEwMjA2MDA1MjUw.YFFzCA.4y0aTZs631ZCh2PRrUDjLgZtUdQ")
