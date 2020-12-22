import discord


async def welcomemsg(client, ctx, type):

    #Text für welcome Channel
    if type == "welcometext":
        embedWelcome = discord.Embed(
            title="Lies dir bitte vor der weiteren Nutzung diese Anleitung durch, damit du weißt, was zu tun ist und wie die Regeln sind.",
            description="Eine Übersicht, was Discord ist und wie es funktioniert, findest du per Klick auf die Überschrift.",
            color=0x26c606)
        embedWelcome.set_author(name="Willkommen auf dem Discord-Server des FSR WiWi",
                         url="https://support.discord.com/hc/de/articles/360045138571?utm_source=discord&utm_medium=blog&utm_campaign=2020-06_help-new-user&utm_content=--t%3Apm",
                         icon_url="https://fsrwiwi.de/wp-content/uploads/2020/10/image940-1024x1014.png")
        embedWelcome.add_field(name="1)",
                        value=" Der Discord-Server wurde für den Immatrikulationsjahrgang 2020 der Fakultät Wirtschaftswissenschaften erstellt. Er dient dem Austausch über das Studium, aber auch zur generellen Vernetzung. Lade bitte Freunde von anderen Fakultäten nur für den Vernetzungsteil ein. Diese sollten nach dem Vernetzungsabend am besten auch den Server wieder verlassen. Zugang gibt es für diese im Startchat über die Eingabe „Gast“.",
                        inline=False)
        embedWelcome.add_field(name="2)",
                        value="Zum Austausch über das Studium existiert für (fast) jeden Kurs eine Kategorie. Hier gibt es jeweils einen Sprachkanal, in welchem du mit Kommiliton*innen die Vorlesungen und Übungen diskutieren kannst. Diese stehen dir ohne Anmeldung frei zur Verfügung und du kannst natürlich auch aktiven Sessions beitreten. Störe dabei aber bitte nicht die Arbeit. Wenn es Fragen an alle gibt oder Neuigkeiten, die jeder mitbekommen sollte, kannst du diese in den zugehörigen Chat schreiben. Diesen kannst du auch nutzen, um mit anderen Termine zum Üben zu vereinbaren. Für Lösungsvorschläge kann gerne der entsprechende Textkanal genutzt werden. Tipp: Klappe aktuell nicht benötigte Kategorien ein. Dadurch wird es bei dir wesentlich übersichtlicher",
                        inline=False)
        embedWelcome.add_field(name="3)",
                        value="Es gibt auch allgemeine Kanäle, welche sich oben in der Liste befinden. Sehr wichtig ist der Feedback-Kanal. Wir wissen, dass zu Beginn noch nicht alles rund laufen wird. Deswegen benötigen wir auf jeden Fall Feedback, was bisher noch nicht so gut läuft, aber auch gerne darüber, was sehr gut läuft. Nur so können wir den Server optimal für euch anpassen. Weiterhin wird es wöchentliche Sprechstunden mit dem FSR geben, in welchem du Fragen zum Studium stellen kannst. Der zugehörige Kanal befindet sich in der Kategorie FSR-Kontakt",
                        inline=False)
        embedWelcome.add_field(name="4)",
                        value="Um dich in diesen Zeiten digital mit anderen vernetzen zu können, haben wir eine entsprechende Kategorie erstellt. Hier kannst du dich zu Spieleabenden oder ähnlichem eintreffen, aber auch wenn du einfach nur mit jemanden reden willst. Für letzteres kannst du dich einfach an einen der virtuellen Bartische setzen und schon geht’s los. Zur Absprache für deine Spieleabende kannst du gerne den zugehörigen Textkanal nutzen. Über diesen werden wir auch eventuelle Events vom FSR kommunizieren.",
                        inline=False)
        embedWelcome.add_field(name="5) Regeln:",
                        value="""1. Respektvoller Umgang miteinander 
                        2. Kein Spam in Kanälen, Privatchats sollten auch privat geführt werden
                        3. Kein unangemessener Inhalt""",
                        inline=False)
        embedWelcome.add_field(name="Wir wünschen viel Spaß :blush:",
                        value="Wenn ihr Hilfe braucht, wendet euch an Mods oder schreibt dem FSR", inline=False)
        await ctx.channel.send(embed=embedWelcome)


    #Text für registrierung Channel
    emojiWing = client.get_emoji(773074983449788416)  # Wing
    emojiWinf = client.get_emoji(773074983798571058)  # Winf
    emojiWiwi = client.get_emoji(773074983579811850)  # Wiwi
    emojiWipaed = client.get_emoji(773074983412301864)  # Wipaed
    emoji2020 = client.get_emoji(774457516108021790)  # 2020
    emoji2019 = client.get_emoji(774457516028985445)  # 2019
    emoji2018 = client.get_emoji(774457515961614339)  # 2018
   
    if type == "register":
        embedUeberschrift = discord.Embed(
            title="Drücke auf die jeweiligen Emoji's, danach wird dir deine Rolle zugewiesen. Wenn du Hilfe benötigst, benutze den Support-Channel.",
            color=0x82fe06)
        await ctx.channel.send(embed=embedUeberschrift)

        embedStudiangangwahl = discord.Embed(
            title="1. Wähle deinen Studiengang:",
            description="    ", color=0x82fe06)
        embedStudiangangwahl.add_field(name="Wirtschaftingeneurwesen {}".format(emojiWing), value="------", inline=False)
        embedStudiangangwahl.add_field(name="Wirtschaftinformatik {}".format(emojiWinf), value="------", inline=False)
        embedStudiangangwahl.add_field(name="Wirtschaftspädagogik {}".format(emojiWipaed), value="------", inline=False)
        embedStudiangangwahl.add_field(name="Wirtschaftswissenschaften {}".format(emojiWiwi), value="------", inline=True)
        mess = await ctx.channel.send(embed=embedStudiangangwahl)
        await mess.add_reaction(emojiWing)
        await mess.add_reaction(emojiWinf)
        await mess.add_reaction(emojiWipaed)
        await mess.add_reaction(emojiWiwi)


        embedImmaJahr = discord.Embed(
            title="2 .Wähle das Jahr deiner Immatrikulation:",
            color=0x82fe06)
        embedImmaJahr.add_field(name="2020 {}".format(emoji2020), value="------", inline=False)
        embedImmaJahr.add_field(name="2019 {}".format(emoji2019), value="------", inline=False)
        embedImmaJahr.add_field(name="2018+ {}".format(emoji2018), value="------", inline=False)
        mess = await ctx.channel.send(embed=embedImmaJahr)
        await mess.add_reaction(emoji2020)
        await mess.add_reaction(emoji2019)
        await mess.add_reaction(emoji2018)

# was ist damit? wird das überhaupt getriggert?
async def confirmmsg(ctx, var):
    await ctx.author.send(
        "Du hast dich erfolgreich für {} registriert! Wenn du sonstige Hilfe benötigst, wende dich bitte an einen Moderator.".format(
            var))
