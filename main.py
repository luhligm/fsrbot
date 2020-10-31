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


@client.event
async def on_member_join(member):
    await welcomemsg(member)
    print(f"{member.author.name} ist beigetreten")
    user = member.message.author
    role = 'Anmeldung'
    await user.add_roles(discord.utils.get(user.guild.roles, name=role))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')
    await ctx.send(ctx.channel.id)


@client.command()   # durch @client.event ersetzen
async def login(ctx):   # on_member_join(member)
    await welcomemsg(ctx)
    print(f"{ctx.author.name} ist beigetreten")
    user = ctx.message.author
    role = 'Anmeldung'
    await user.add_roles(discord.utils.get(user.guild.roles, name=role))


@client.command()
async def wipad(ctx):
    role = 'wipäd'
    if rolecheck(ctx.author, 'Anmeldung') and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await user.remove_roles(discord.utils.get(user.guild.roles, name='Anmeldung'))
        await confirmmsg(ctx, 'WPädagogik')

@client.command()
async def winf(ctx):
    role = 'winf'
    if rolecheck(ctx.author, 'Anmeldung') and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await user.remove_roles(discord.utils.get(user.guild.roles, name='Anmeldung'))
        await confirmmsg(ctx, 'WInformatik')


@client.command()
async def wing(ctx):
    role = 'wing'
    if rolecheck(ctx.author, 'Anmeldung') and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await user.remove_roles(discord.utils.get(user.guild.roles, name='Anmeldung'))
        await confirmmsg(ctx, 'WIngeneurswesen')


@client.command()
async def wiwi(ctx):
    role = 'wiwi'
    if rolecheck(ctx.author, 'Anmeldung') and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await user.remove_roles(discord.utils.get(user.guild.roles, name='Anmeldung'))
        await confirmmsg(ctx, 'WWissenschaften')


client.run(pw.TOKEN)
