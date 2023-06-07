import discord 
from discord.ext import commands
import time
import typing
import random
intents = discord.Intents().all()
Gilbert27 = commands.Bot(command_prefix=".",intents=intents)

@Gilbert27.command()
async def say(ctx , * , message):
    await ctx.reply(message)

@Gilbert27.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@Gilbert27.event 
async def on_member_remove(member):
    print(f'{member} has left the server.')
    
@Gilbert27.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')

@Gilbert27.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@Gilbert27.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

Gilbert27.run("token")
