import discord
from mongodb import getUser


# wenn in keiner Rolle dann True


def giveRole(user):
    jg = getUser(user.id)['jg']
    sg = getUser(user.id)['sg']
    if sg == 'winf':
        if jg == '2020':
            return 'WInformatik2020'
        elif jg == '2019':
            return 'WInformatik2019'
        elif jg == '2018':
            return 'WInformatik2018'
    elif sg == 'wing':
        if jg == '2020':
            return 'WIngeneur2020'
        elif jg == '2019':
            return 'WIngeneur2019'
        elif jg == '2018':
            return 'WIngeneur2018'
    elif sg == 'wiwi':
        if jg == '2020':
            return 'WWissenschaften2020'
        elif jg == '2019':
            return 'WWissenschaften2019'
        elif jg == '2018':
            return 'WWissenschaften2018'
    elif sg == 'wipad':
        if jg == '2020':
            return 'WPädagoge2020'
        elif jg == '2019':
            return 'WPädagoge2019'
        elif jg == '2018':
            return 'WPädagoge2018'


