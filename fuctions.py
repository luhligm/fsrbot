import discord
from pw import channelID


# Test ob Rolle schon vergeben ist, dass man keine zwei Kurse bekommen kann

def rolecheck(user, roletocheck):

    role = discord.utils.get(user.guild.roles, name=roletocheck)

    if role in user.roles:
        return True
    else:
        return False

    roles = ['winf', 'wipäd', 'wing']

    if roletocheck == 'Anmeldung':
        print("hey")
        if role in roles:
            return True
        else:
            return False


# Test ob Nachricht in hinterlegtem Channel gesendet wurde

def isRegisterChannel(ctx):
    if ctx.channel.id == channelID:
        return True
