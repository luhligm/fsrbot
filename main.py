import asyncio
import discord
import datetime
from discord.ext import commands
from mongodb import alreadyExists, collection, getUser, editUser, getConfig
from fuctions import giveRole
from msgcontent import welcomemsg, confirmmsg

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('[FSRBot] Script erfolgreich geladen')
    print(f'[FSRBot] Bot online ({round(client.latency * 1000)} ms)')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')


@client.listen('on_message')
async def autodelete(message):
    if message.channel.id == getConfig('regChannel') and not message.author.bot:
        await asyncio.sleep(1)
        await message.delete()


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if payload.member.bot:
        return

    if channel.id == getConfig('regChannel'):
        user = payload.member

        if alreadyExists(user.id) is False:
            post = {'_id': user.id, 'displayName': user.name, 'joinTime': datetime.datetime.utcnow(), 'role': "not set",
                    'isRegSG': False, 'isRegJG': False}
            collection.insert_one(post)

        if getUser(user.id)['role'] == "not set":
            if message.id == getConfig('firstRegMsg'):
                if payload.emoji.name == 'winf':
                    editUser(user.id, 'sg', 'winf')
                if payload.emoji.name == 'wiwi':
                    editUser(user.id, 'sg', 'wiwi')
                if payload.emoji.name == 'wipad':
                    editUser(user.id, 'sg', 'wipad')
                if payload.emoji.name == 'wing':
                    editUser(user.id, 'sg', 'wing')
                editUser(user.id, 'isRegSG', True)

            if message.id == getConfig('secondRegMsg'):
                if payload.emoji.name == 'fsr20':
                    editUser(user.id, 'jg', '2020')
                if payload.emoji.name == 'fsr19':
                    editUser(user.id, 'jg', '2019')
                if payload.emoji.name == '2018+':
                    editUser(user.id, 'jg', 'fsr18')
                editUser(user.id, 'isRegJG', True)

        if getUser(user.id)['isRegSG'] and getUser(user.id)['isRegJG']:
            print('beides wurde gewählt')
            role = giveRole(user)
            print(role)
            editUser(user.id, 'role', role)
            await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        else:
            print('noch nicht beides ausgewählt')
    await message.remove_reaction(payload.emoji, user)


@client.command()
async def createmsg(ctx, arg):
    e1 = client.get_emoji(773074983449788416)   # Wing
    e2 = client.get_emoji(773074983798571058)   # Winf
    e3 = client.get_emoji(773074983579811850)   # Wiwi
    e4 = client.get_emoji(773074983412301864)   # Wipad
    e5 = client.get_emoji(774457516108021790)   # 2020
    e6 = client.get_emoji(774457516028985445)   # 2019
    e7 = client.get_emoji(774457515961614339)   # 2018
    await welcomemsg(ctx, arg, e1, e2, e3, e4, e5, e6, e7)


client.run(getConfig('TOKEN'))
