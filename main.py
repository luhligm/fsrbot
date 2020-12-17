# Einstiegspunkt des Pythonsscript

import asyncio
import discord
from datetime import *
from discord.ext import commands
from mariadbConnector import *
from fuctions import giveRole
from msgcontent import welcomemsg, confirmmsg

"""
erzeugt Instanz von Client
Client ist die Verbindung zum Discordserver
Der Client reagiert auf alle nachrichten mit dem Präfix (!)
"""
client = commands.Bot(command_prefix="!")

#Ausgabe ob Bot erfolgreich gestartet und Client Latency in Terminal nach Start des Scripts
@client.event
async def on_ready():
    print('[FSRBot] Script erfolgreich geladen und der Client hat eine Verbindung zum Server aufgebaut')
    print(f'[FSRBot] Bot online ({round(client.latency * 1000)} ms)')

#Test Ping, Antwort Ping, was ist der Trigger?
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')



# erzeugt message für welcome- und registrierungschannel
@client.command()
async def createmsg(ctx, arg):

    await welcomemsg(client, ctx, arg)


# Löscht Nachricht
@client.listen('on_message')
async def autodelete(message):
    if message.channel.id == getConfig('regChannel') and not message.author.bot:
        await asyncio.sleep(1)
        await message.delete()


# Event, dass auf Auswahl der Emoji reagiert (payload = message data)
@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    # keine Reaktion, fall der Bot der Auslöser war
    if payload.member.bot:
        return

    # reagiert nur auf Emoji im registrierung Channel
    if channel.id == getConfig('regChannel'):
        user = payload.member

        # User ist noch nicht in der Datenbank
        if userAlreadyExists(user.id) is False:
            joinTime = datetime.now()
            addUser(user.id,user.name,joinTime,)

        # User ist schon in der Datenbank, hat aber noch keine Rolle
        # woher kommt payload.emoji.name ?
        if getAllUserEigenschaften(user.id)['role'] == None:
            if message.id == getConfig('firstRegMsg'):
                if payload.emoji.name == 'winf':
                    editUser(user.id, studiengang = 'winf')
                if payload.emoji.name == 'wiwi':
                    editUser(user.id, studiengang = 'wiwi')
                if payload.emoji.name == 'wipad':
                    editUser(user.id, studiengang = 'wipad')
                if payload.emoji.name == 'wing':
                    editUser(user.id, studiengang = 'wing')

            if message.id == getConfig('secondRegMsg'):
                if payload.emoji.name == 'fsr20':
                    editUser(user.id, jahrgang =  '2020')
                if payload.emoji.name == 'fsr19':
                    editUser(user.id, jahrgang = '2019')
                if payload.emoji.name == '2018+':
                    editUser(user.id, jahrgang = 'fsr18')


        # user hat beide emoji ausgewählt -> bekommt Rollen
        if getAllUserEigenschaften(user.id)['jahrgang'] and getAllUserEigenschaften(user.id)['studiengang']:
            print('beides wurde gewählt')
            role = giveRole(user)
            print(role)
            editUser(user.id, role= role)
            await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        else:
            print('noch nicht beides ausgewählt')

    # entfernt Reaktion auf den Emoji
    await message.remove_reaction(payload.emoji, user)

# startet den Client
client.run(getConfig('TOKEN'))
