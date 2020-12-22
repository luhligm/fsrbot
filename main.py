# Einstiegspunkt des Pythonsscript

import asyncio
import discord
from datetime import *
from discord.ext import commands
from mariadbConnector import *
from fuctions import matchJahrgangAndStudiengangToRole
from msgcontent import welcomemsg, confirmmsg
from user import User
import config


"""
erzeugt Instanz von Client
Client ist die Verbindung zum Discordserver
Der Client reagiert auf alle nachrichten mit dem Präfix (!)
"""
client = commands.Bot(command_prefix="!")
config = config.Config()


#Ausgabe ob Bot erfolgreich gestartet und Client Latency in Terminal nach Start des Scripts
@client.event
async def on_ready():
    print('[FSRBot] Script erfolgreich geladen und der Client hat eine Verbindung zum Server aufgebaut')
    print(f'[FSRBot] Bot online ({round(client.latency * 1000)} ms)')

#Test Ping, Antwort Ping, was ist der Trigger?
@client.command()
@commands.has_role("Ping")
async def ping(ctx):
    await ctx.send(f'Pong --> {round(client.latency * 1000)} ms')



# erzeugt message für welcome- und registrierungschannel
@client.command()
@commands.has_role("Chef")
async def createmsg(ctx, arg):

    await welcomemsg(client, ctx, arg)


# Löscht Nachricht
@client.listen('on_message')
async def autodelete(message):
    if message.channel.id == config.regChannel and not message.author.bot:
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
    print('kein Bot')
    # reagiert nur auf Emoji im registrierung Channel
    if channel.id == config.regChannel:
        print('im Reg Channel')
        #User wird in der Datenbank angelegt oder seine Eingeschaften werden aus der Datenbank geleden
        user = User(payload.member.id, payload.member.name)

        # User ist schon in der Datenbank, hat aber noch keine Rolle
        if user.role == None:
            print('user hat noch keine Rolle')

            if message.id == config.firstRegMsg:
                print('setstudiengang: ',payload.emoji.name)
                if payload.emoji.name == 'winf':
                    user.setStudiengang('winf')
                if payload.emoji.name == 'wiwi':
                    user.setStudiengang('wiwi')
                if payload.emoji.name == 'wipaed':
                    user.setStudiengang('wipaed')
                if payload.emoji.name == 'wing':
                    user.setStudiengang('wing')

            print(message.id == config.secondRegMsg)
            if message.id == config.secondRegMsg:
                print('setjahrgang: ',payload.emoji.name)
                if payload.emoji.name == 'fsr20':
                    user.setJahrgang('2020')
                if payload.emoji.name == 'fsr19':
                    user.setJahrgang('2019')
                if payload.emoji.name == 'fsr18':
                    user.setJahrgang('2018')



        # user hat beide emoji ausgewählt (hat Studiengang und Jahrgang) -> bekommt Rolle
        if user.jahrgang and user.studiengang:
            print('beides wurde gewählt')
            print(user.studiengang,user.jahrgang)
            role = matchJahrgangAndStudiengangToRole(user)
            print('role: ',role,type(role))
            user.setRole(role)
            await payload.member.add_roles(discord.utils.get(payload.member.guild.roles, name=role))
        else:
            print('noch nicht beides ausgewählt')

    # entfernt Reaktion auf den Emoji
    await message.remove_reaction(payload.emoji, payload.member)

@client.event
async def on_member_remove(member):
    user = User(member.id, member.name)
    user.setLeaveTime()
    print('User: ',user.name,' hat den Server verlassen')




# startet den Client
client.run(config.botToken)
# connection.close()
