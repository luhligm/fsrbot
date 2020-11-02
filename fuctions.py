import discord
from pw import channelID


# Test ob Rolle schon vergeben ist, dass man keine zwei Kurse bekommen kann

def rolecheck(user):
    role1 = discord.utils.get(user.guild.roles, name='WInformatiker')
    role2 = discord.utils.get(user.guild.roles, name='WIngeneur')
    role3 = discord.utils.get(user.guild.roles, name='WPädagoge')
    role4 = discord.utils.get(user.guild.roles, name='WWissenschaftler')

    if role1 in user.roles:
        return False
    elif role2 in user.roles:
        return False
    elif role3 in user.roles:
        return False
    elif role4 in user.roles:
        return False
    else:
        return True


# Test ob Nachricht in hinterlegtem Channel gesendet wurde

def isRegisterChannel(ctx):
    if ctx.channel.id == channelID:
        return True
