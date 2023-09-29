
import discord, asyncio
from discord.ext import commands

with open('token.txt', 'r') as file:
    token = file.read()[:-1]
description = "I run games of Mafia. Type ?newgame to begin a game, or ?help for help"

bot = commands.Bot(command_prefix='?', description=description)
# bot.remove_command('help')
