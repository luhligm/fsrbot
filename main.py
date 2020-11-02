import asyncio

import discord
from discord import member
from discord.ext import commands

import pw
from fuctions import rolecheck, channelID, isRegisterChannel
from msgcontent import welcomemsg, confirmmsg

client = commands.Bot(command_prefix="!")
client2 = discord.Client()


@client.event
async def on_ready():
    print('geladen')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')
    await ctx.send(ctx.channel.id)


@client.command()  # durch @client.event ersetzen
async def login(ctx):  # on_member_join(member)
    print(f"{ctx.author.name} ist beigetreten")
    user = ctx.message.author
    role = 'Anmeldung'


@client.command()
async def wipad(ctx):
    role = 'wipäd'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WPädagogik')


@client.command()
async def winf(ctx):
    role = 'winf'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WInformatik')


@client.command()
async def wing(ctx):
    role = 'wing'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WIngeneurswesen')


@client.command()
async def wiwi(ctx):
    role = 'wiwi'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WWissenschaften')


@client.listen('on_message')
async def autodelete(message):
    if isRegisterChannel(message):
        await asyncio.sleep(1)
        await message.delete()


client.run(pw.TOKEN)
