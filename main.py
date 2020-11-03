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
    await welcomemsg(ctx)


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
    channel = client.get_channel(pw.channelhilfe)
    emo = client.get_emoji(773017948037185536)
    await hilfemsg(ctx, channel, arg, emo)
    await ctx.author.send("Deine Anfrage wurde gesendet")


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if payload.member.bot:
        return

    if channel.id == pw.channelID and message.id == 773071590535331910:
        user = payload.member
        print(payload)
        if rolecheck(user):
            if payload.emoji.name == 'winf':
                await user.add_roles(discord.utils.get(user.guild.roles, name='winf'))
            if payload.emoji.name == 'wiwi':
                await user.add_roles(discord.utils.get(user.guild.roles, name='wiwi'))
            if payload.emoji.name == 'wipad':
                await user.add_roles(discord.utils.get(user.guild.roles, name='wipäd'))
            if payload.emoji.name == 'wing':
                await user.add_roles(discord.utils.get(user.guild.roles, name='wing'))
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
    e1 = client.get_emoji(773058764181995541)
    e2 = client.get_emoji(773058763930337280)
    e3 = client.get_emoji(773058764277284864)
    e4 = client.get_emoji(773058763950653450)
    await welcomemsg(ctx, e1, e2, e3, e4)


client.run(pw.TOKEN)
