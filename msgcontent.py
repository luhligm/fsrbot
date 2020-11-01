import discord


async def welcomemsg(ctx):
    embed = discord.Embed(
        title="lies dir bitte vor der weiteren Nutzung diese Anleitung durch, damit du weißt, was zu tun ist und wie die Regeln sind.",
        description="-----", color=0x82fe06)
    embed.set_author(name="Willkommen auf dem Discord-Server des FSR WiWi",
                     icon_url="https://fsrwiwi.de/wp-content/uploads/2020/10/image940-1024x1014.png")
    embed.add_field(name="1.",
                    value="Der Discord-Server wurde für den Immatrikulationsjahrgang 2020 der Fakultät Wirtschaftswissenschaften erstellt. Er dient dem Austausch über das Studium, aber auch zur generellen Vernetzung. Lade bitte Freunde von anderen Fakultäten nur für den Vernetzungsteil ein. Diese sollten nach dem Vernetzungsabend am besten auch den Server wieder verlassen. Zugang gibt es im Startchat über die Eingabe „Gast“.",
                    inline=False)
    embed.add_field(name="2.",
                    value="Zum Austausch über das Studium existiert für (fast) jeden Kurs eine Kategorie. Hier gibt es jeweils 3 Sprachkanäle, in welchem du mit Kommiliton*innen die Vorlesungen und Übungen diskutieren kannst. Wenn es Fragen an alle gibt oder Neuigkeiten, die jeder mitbekommen sollte, kannst du diese in den zugehörigen Chat schreiben. Diesen kannst du auch nutzen, um mit anderen Termine zum Üben zu vereinbaren. Für Lösungsvorschläge kann gerne der entsprechende Textkanal genutzt werden. Tipp: Klappe aktuell nicht benötigte Kategorien ein. Dadurch wird es bei dir wesentlich übersichtlicher.",
                    inline=False)
    embed.add_field(name="3.",
                    value="Es gibt auch allgemeine Kanäle. Sehr wichtig ist der Feedback-Kanal. Wir wissen, dass zu Beginn noch nicht alles rund laufen wird. Deswegen benötigen wir auf jeden Fall Feedback, was bisher noch nicht so gut läuft, aber auch gerne darüber, was sehr gut läuft. Nur so können wir den Server optimal für euch anpassen. Weiterhin wird es wöchentliche Sprechstunden mit dem FSR geben, in welchem du Fragen zum Studium stellen kannst. Diese können aber auch im entsprechenden Textkanal gestellt werden.",
                    inline=False)
    embed.add_field(name="4.",
                    value="Um dich in diesen Zeiten digital mit anderen vernetzen zu können, haben wir eine entsprechende Kategorie erstellt. Hier kannst du dich zu Spieleabenden oder ähnlichem eintreffen, aber auch wenn du einfach nur mit jemanden reden willst. Für letzteres kannst du dich einfach an einen der virtuellen Bartische setzen und schon geht’s los.",
                    inline=False)
    embed.add_field(name="5.",
                    value="Bitte verhalte dich respektvoll gegenüber anderen. Wir behalten uns vor, Leute zu entfernen, falls uns negatives berichtet wird.",
                    inline=False)
    await ctx.channel.send(embed=embed)

    embed2 = discord.Embed(
        title="Du musst dich nun noch mit deinem Studiengang registrieren, schreibe dafür den jeweiligen Befehl in den Anmeldungs-Textchannel:",
        description="------", color=0x82fe06)
    embed2.add_field(name="Wirtschaftingeneurwesen", value="!wing", inline=False)
    embed2.add_field(name="Wirtschaftinformatik", value="!winf", inline=False)
    embed2.add_field(name="Wirtschaftspädagogik", value="!wipad", inline=False)
    embed2.add_field(name="Wirtschaftswissenschaften", value="!wiwi", inline=True)
    embed2.set_footer(
        text="Sollte dir keine Rolle zugewiesen werden oder ein anderer Fehler auftreten, benutze !hilfe . Der Bot befinden sich noch in der Entwicklung, für Bugs möchten wir uns entschuldigen.")
    await ctx.channel.send(embed=embed2)


async def confirmmsg(ctx, var):
    await ctx.author.send(
        "Du hast dich erfolgreich für {} registriert! Wenn du sonstige Hilfe benötigst, wende dich bitte an einen Moderator.".format(
            var))
