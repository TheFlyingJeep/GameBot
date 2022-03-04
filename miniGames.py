import PIL, requests, asyncio, discord, youtube_dl, ytmusicapi, random
import discord.errors as err, discord.utils as ut
import matplotlib.pyplot as plt


class minigames:
    def __init__(self, count):
        self.players = {}
        self.gamecount = count
        self.ongame = 1
        self.games = [typingGame(self), trivia(self), hangman(self), imposter(self), guessImage(self), guessMessage(self), roles(self), pythonProgram(self)]

    async def choosegame(self):
        if self.ongame <= self.gamecount:
            i = random.randint(0, len(self.games))
            await self.games[i]
            del self.games[i]
        else:
            await endGame(self)


async def typingGame(game):
    print(game)

async def trivia(game):
    print(game)

async def hangman(game):
    print(game)

async def imposter(game):
    print(game)

async def guessImage(game):
    print(game)

async def guessMessage(game):
    print(game)

async def roles(game):
    print(game)

async def pythonProgram(game):
    print(game)

async def endGame(game):
    del game