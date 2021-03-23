import discord
from discord.ext import commands
from random import randint
import random
import os
import youtube_dl


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #tictactoe 

    @commands.group(invoke_without_command=True)
    async def ttt(self, ctx):
        """Jogo da velha."""
        pass

    @ttt.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member = None):
        """Use o comando para começar a jogar."""
        if p2 == None:
            p2 = ctx.author
        global player1
        global player2
        global turn
        global gameOver
        global count

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",]
            
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            #print the board

            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x] 
            
            #determina qm vai primeiro

            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("É a vez de: <@" + str(player1.id) + ">.")
            elif num == 2:
                turn = player2
                await ctx.send("Sua vez <@" + str(player2.id) +">.")
        else:
            await ctx.send("Já tem um jogo acontecendo.")
    @ttt.command()
    async def place(self, ctx, pos : int):
        """Coloca X ou O na posição desejada"""
        global turn
        global player1
        global player2
        global board 
        global count 
        global gameOver

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board [pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1 

                    
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x] 
                    
                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " Você ganhou.")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Empate.")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1

                else:
                    await ctx.send("Tenha certeza de escolher um algarismo entre 1 e 9 e um quadrado que não está marcado.")
            else:
                await ctx.send("Aguarde a sua vez.")
        else:
            await ctx.send("Comece outro jogo.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

def setup(client):
    client.add_cog(Misc(client))