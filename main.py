import asyncio

import discord
from discord import member
from discord.ext import commands

import pw
from fuctions import rolecheck, channelID, isRegisterChannel
from msgcontent import welcomemsg, confirmmsg, hilfemsg

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('geladen')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')


@client.command()
async def wipad(ctx):
    role = 'WPädagoge'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WPädagogik')


@client.command()
async def winf(ctx):
    role = 'WInformatiker'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WInformatik')


@client.command()
async def wing(ctx):
    role = 'WIngeneur'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WIngeneurswesen')


@client.command()
async def wiwi(ctx):
    role = 'WWissenschaftler'
    if rolecheck(ctx.author) and isRegisterChannel(ctx):
        user = ctx.message.author
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await confirmmsg(ctx, 'WWissenschaften')


@client.listen('on_message')
async def autodelete(message):
    if isRegisterChannel(message) and not message.author.bot:
        await asyncio.sleep(1)
        await message.delete()


@client.command()
async def hilfe(ctx, *, arg):
    if ctx.author.bot:
        return
    channel = client.get_channel(pw.channelhilfe)
    emo = client.get_emoji(773074983831863307)
    await hilfemsg(ctx, channel, arg, emo)
    await ctx.author.send(f"Deine Anfrage wurde gesendet ({arg})")


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if payload.member.bot:
        return

    if channel.id == pw.channelID and message.id == pw.regmess:
        user = payload.member
        print(payload)
        if rolecheck(user):
            if payload.emoji.name == 'winf':
                await user.add_roles(discord.utils.get(user.guild.roles, name='WInformatiker'))
            if payload.emoji.name == 'wiwi':
                await user.add_roles(discord.utils.get(user.guild.roles, name='WWissenschaftler'))
            if payload.emoji.name == 'wipad':
                await user.add_roles(discord.utils.get(user.guild.roles, name='WPädagoge'))
            if payload.emoji.name == 'wing':
                await user.add_roles(discord.utils.get(user.guild.roles, name='WIngeneur'))
            await message.remove_reaction(payload.emoji, user)

    if channel.id == pw.channelhilfe:
        if payload.emoji.name == 'SOLVED':
            dict_embed = message.embeds[0].to_dict()
            dict_embed['color'] = 0x26c606

            id = int(dict_embed['fields'][0]['value'])
            user = client.get_user(id)

            new_embed = discord.Embed.from_dict(dict_embed)
            new_embed.set_author(name="GESCHLOSSEN")

            await user.send("Deine Anfrage wurde bearbeitet")
            await message.delete()
            await channel.send(embed=new_embed)


@client.command()
async def createreg(ctx):
    e1 = client.get_emoji(773074983798571058)
    e2 = client.get_emoji(773074983449788416)
    e3 = client.get_emoji(773074983579811850)
    e4 = client.get_emoji(773074983412301864)
    await welcomemsg(ctx, e1, e2, e3, e4)


client.run(pw.TOKEN)
