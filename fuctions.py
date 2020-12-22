import discord


# wenn in keiner Rolle dann True
# gibt einem User Rollen
#todo Funktion in User Überführen
def matchJahrgangAndStudiengangToRole(user):
    jahrgang = user.jahrgang
    print('jahrgang ',jahrgang)
    studiengang = user.studiengang
    print('studiengang: ',studiengang)
    if studiengang == 'winf':
        if jahrgang == '2020':
            return 'WInformatik2020'
        elif jahrgang == '2019':
            return 'WInformatik2019'
        elif jahrgang == '2018':
            return 'WInformatik2018'
    elif studiengang == 'wing':
        if jahrgang == '2020':
            return 'WIngeneur2020'
        elif jahrgang == '2019':
            return 'WIngeneur2019'
        elif jahrgang == '2018':
            return 'WIngeneur2018'
    elif studiengang == 'wiwi':
        if jahrgang == '2020':
            return 'WWissenschaften2020'
        elif jahrgang == '2019':
            return 'WWissenschaften2019'
        elif jahrgang == '2018':
            return 'WWissenschaften2018'
    elif studiengang == 'wipaed':
        if jahrgang == '2020':
            return 'WPädagoge2020'
        elif jahrgang == '2019':
            return 'WPädagoge2019'
        elif jahrgang == '2018':
            return 'WPädagoge2018'
    elif studiengang == 'master':
        return 'Master'
