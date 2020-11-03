import discord


async def welcomemsg(ctx, e1, e2, e3, e4):
    embed = discord.Embed(
        title="Lies dir bitte vor der weiteren Nutzung diese Anleitung durch, damit du weißt, was zu tun ist und wie die Regeln sind.",
        description="Eine Übersicht, was Discord ist und wie es funktioniert, findest du per Klick auf die Überschrift.",
        color=0x26c606)
    embed.set_author(name="Willkommen auf dem Discord-Server des FSR WiWi",
                     url="https://support.discord.com/hc/de/articles/360045138571?utm_source=discord&utm_medium=blog&utm_campaign=2020-06_help-new-user&utm_content=--t%3Apm",
                     icon_url="https://fsrwiwi.de/wp-content/uploads/2020/10/image940-1024x1014.png")
    embed.add_field(name="1)",
                    value=" Der Discord-Server wurde für den Immatrikulationsjahrgang 2020 der Fakultät Wirtschaftswissenschaften erstellt. Er dient dem Austausch über das Studium, aber auch zur generellen Vernetzung. Lade bitte Freunde von anderen Fakultäten nur für den Vernetzungsteil ein. Diese sollten nach dem Vernetzungsabend am besten auch den Server wieder verlassen. Zugang gibt es für diese im Startchat über die Eingabe „Gast“.",
                    inline=False)
    embed.add_field(name="2)",
                    value="Zum Austausch über das Studium existiert für (fast) jeden Kurs eine Kategorie. Hier gibt es jeweils einen Sprachkanal, in welchem du mit Kommiliton*innen die Vorlesungen und Übungen diskutieren kannst. Diese stehen dir ohne Anmeldung frei zur Verfügung und du kannst natürlich auch aktiven Sessions beitreten. Störe dabei aber bitte nicht die Arbeit. Wenn es Fragen an alle gibt oder Neuigkeiten, die jeder mitbekommen sollte, kannst du diese in den zugehörigen Chat schreiben. Diesen kannst du auch nutzen, um mit anderen Termine zum Üben zu vereinbaren. Für Lösungsvorschläge kann gerne der entsprechende Textkanal genutzt werden. Tipp: Klappe aktuell nicht benötigte Kategorien ein. Dadurch wird es bei dir wesentlich übersichtlicher",
                    inline=False)
    embed.add_field(name="3)",
                    value="Es gibt auch allgemeine Kanäle, welche sich oben in der Liste befinden. Sehr wichtig ist der Feedback-Kanal. Wir wissen, dass zu Beginn noch nicht alles rund laufen wird. Deswegen benötigen wir auf jeden Fall Feedback, was bisher noch nicht so gut läuft, aber auch gerne darüber, was sehr gut läuft. Nur so können wir den Server optimal für euch anpassen. Weiterhin wird es wöchentliche Sprechstunden mit dem FSR geben, in welchem du Fragen zum Studium stellen kannst. Der zugehörige Kanal befindet sich in der Kategorie FSR-Kontakt",
                    inline=False)
    embed.add_field(name="4)",
                    value="Um dich in diesen Zeiten digital mit anderen vernetzen zu können, haben wir eine entsprechende Kategorie erstellt. Hier kannst du dich zu Spieleabenden oder ähnlichem eintreffen, aber auch wenn du einfach nur mit jemanden reden willst. Für letzteres kannst du dich einfach an einen der virtuellen Bartische setzen und schon geht’s los. Zur Absprache für deine Spieleabende kannst du gerne den zugehörigen Textkanal nutzen. Über diesen werden wir auch eventuelle Events vom FSR kommunizieren.",
                    inline=False)
    embed.add_field(name="5) Regeln:",
                    value="""1. Respektvoller Umgang miteinander 
                    2. Kein Spam in Kanälen, Privatchats sollten auch privat geführt werden
                    3. Kein unangemessener Inhalt""",
                    inline=False)
    embed.add_field(name="Wir wünschen viel Spaß :blush:",
                    value="Wenn ihr Hilfe braucht, wendet euch an Mods oder schreibt dem FSR", inline=False)
    await ctx.channel.send(embed=embed)

    embed2 = discord.Embed(
        title="Um deinen Zugang freizuschalten, musst du dich registrieren. Schreibe dafür einfach den jeweiligen Befehl in diesen Channel hier: ",
        description="------", color=0x82fe06)
    embed2.add_field(name="Wirtschaftingeneurwesen", value="!wing", inline=False)
    embed2.add_field(name="Wirtschaftinformatik", value="!winf", inline=False)
    embed2.add_field(name="Wirtschaftspädagogik", value="!wipad", inline=False)
    embed2.add_field(name="Wirtschaftswissenschaften", value="!wiwi", inline=True)
    embed2.set_footer(
        text="Sollte dir keine Rolle zugewiesen werden oder ein anderer Fehler auftreten, benutze !hilfe <Grund> . Der Bot befinden sich noch in der Entwicklung, für Bugs möchten wir uns entschuldigen.")
    mess = await ctx.channel.send(embed=embed2)
    await mess.add_reaction(e1)
    await mess.add_reaction(e2)
    await mess.add_reaction(e3)
    await mess.add_reaction(e4)

async def confirmmsg(ctx, var):
    await ctx.author.send(
        "Du hast dich erfolgreich für {} registriert! Wenn du sonstige Hilfe benötigst, wende dich bitte an einen Moderator.".format(
            var))


async def hilfemsg(ctx, channel, arg, emo):
    embed = discord.Embed(title="{}".format(ctx.author.name), color=0xfe0101)
    embed.set_author(name="OFFEN",
                     icon_url=ctx.author.avatar_url)
    embed.add_field(name="id:", value=ctx.author.id, inline=False)
    embed.add_field(name="Grund:", value=arg, inline=False)
    mess = await channel.send(embed=embed)
    await mess.add_reaction(emo)

