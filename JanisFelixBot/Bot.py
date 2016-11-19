# -*- coding: iso-8859-1 -*-
import random
import time
from chatter.telegramBot import TelegramBot
bot=TelegramBot("244398565:AAEStN15qrHb8noq-ymt_9Bq9T0buri23bY")
bot.gehe_online()
otherbots = open("otherbots.txt").readlines()
admins = open("admins.txt").readlines()
blacklist = open("blacklist.txt").readlines()
for x in range(0,len(admins)) :
    admins[x] = admins[x].rstrip()
print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "] Der Bot wurde erfolgreich gestartet! Die IDs der Admins sind: " + str(admins)))
helptext = open("messages/help.txt").read()
def alarm(verstoss):
    send = ("Achtung! Der User " + str(uservorname) + " (" + str(userid) + ") hat versucht die folgende Sache zu machen: \n " + str(verstoss))
    bot.sende_nachricht(send, -151573627, markdown=True)
    print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "]" + send))
    bot.sende_nachricht("Du bist kein Admin, Anzeige ist raus!", chatid, nachrichtid)

while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        uservorname=nachrichtraw.sender.vorname
        nachrichtid=nachrichtraw.id
        answereduserid=0
        if (nachrichtraw.antwort == None):
            answered="no"
        else:
            answereduserid=nachrichtraw.antwort.sender.id
            answered="yes"
        if (nachrichtraw.inhalt != None and str(userid) not in blacklist):
            message=nachrichtraw.inhalt.split()
            command=message[0].split("@")
            if (command[0]== "/start"):
                bot.sende_nachricht("Hallo, ich bin der *Janisfelixbot*! Programmiert haben mich @flixlix und @sonixier mithilfe von [Felix's Fork der vereinfachten Bot-API](https://github.com/Flixlix/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin! Schreibe /help fï¿½r eine Liste der Befehle.", chatid, nachrichtid, markdown=True)

            if (command[0] == "/id"):
                send="Chat-ID: "+ str(chatid) + "\n Deine ID: " + str(userid) + "\n Vorname: " + str(uservorname)
                if (answered == "yes"):
                    send=send + "\n Die ID der Person, auf die du geantwortet hast:" + str(answereduserid)
                bot.sende_nachricht(send, chatid, nachrichtid)

            if (command[0] == "/null"):
                bot.sende_nachricht("", chatid)

            if (command[0] == "/echo"):
                if (len(message) > 1):
                    words = len(message)
                    send = "*" + uservorname + " sagt:* \n \n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, chatid, markdown=True)
                else:
                    bot.sende_nachricht(
                        "Bitte schicke mir diesen Command so: \n /echo `<Dein Text>` \n Gibt deinen Text aus. *Markdown* wird unterstï¿½tzt!", chatid, nachrichtid, markdown=True)

            if (command[0] == "/markdown"):
                bot.sende_nachricht("Es gibt die folgenden Formatierungen: \n*bold*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk)", chatid, nachrichtid, markdown=True)
                bot.sende_nachricht("Diese sind wie folgt anzuwenden: \n*bold*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk)", chatid, nachrichtid)

            if (command[0] == "/time"):
                datum = str(time.strftime("%d.%m.%Y"))
                zeit = str(time.strftime(" %H:%M:%S"))
                bot.sende_nachricht("Datum: " + str(datum) + "\nUhrzeit:" + str(zeit), chatid, nachrichtid)

            if (command[0] == "/random"):
                if (len(message) > 1):
                    from random import randint
                    randomzahl = randint(0, 6)
                    if randomzahl == 0:
                            words = len(message)
                            send = " " + str(uservorname) + " gibt "
                            for x in range(1, words):
                                send = send + message[x] + " einen Keks."
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 1:
                            words = len(message)
                            send = " " + str(uservorname) + "?? "
                            for x in range(1, words):
                                send = send + message[x] + "!"
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 2:
                            words = len(message)
                            send = " "
                            for x in range(1, words):
                                send = send + message[x] + " liebt Lua."
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 3:
                            words = len(message)
                            send = " "
                            for x in range(1, words):
                                send = send + str(uservorname) + " küsst "
                                send = send + message[x] + " leidenschaftlich."
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 4:
                            words = len(message)
                            send = " "
                            for x in range(1, words):
                                send = send + message[x] + " mag TouchWiz. "
                                send = send + str(uservorname) + " hingegen versucht ihm CyanogenMod aufzuquatschen."
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 5:
                            words = len(message)
                            send = " "
                            for x in range(1, words):
                                send = send + message[x] + " ist ein typischer Fall von einem gerissenen Kondom."
                                bot.sende_nachricht(send, chatid)
                                break
                    if randomzahl == 6:
                            words = len(message)
                            send = "Sag "
                            for x in range(1, words):
                                send = send + message[x] + ", er soll sich verstecken. Die Müllabfuhr kommt!"
                                bot.sende_nachricht(send, chatid)
                                break
                else:
                    bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: /random `<Dein Objekt/Person...>`", chatid, markdown=True)
            if (command[0] == "/help"):
                if str(userid) in admins:
                   adminhelp = helptext + "\n/admincommands - Sende commands für Admins"
                   bot.sende_nachricht(adminhelp, chatid, nachrichtid, markdown=True)
                   break
                else:
                    bot.sende_nachricht(helptext, chatid, nachrichtid, markdown=True)
            if (command[0] == "/feedback"):
                if (len(message) > 1):
                    words = len(message)
                    send = "Ein feedback von " + uservorname + "(" + str(userid) + ") wurde gesendet. \n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, -151573627)
                    bot.sende_nachricht("Dein Feedback wurde versendet! Wir werden dich kontaktieren!", chatid)
                else:
                    bot.sende_nachricht(
                        "Bitte schicke mir diesen Command so: \n /feedback `<Deine VerbesserungsvorschlÃ¤ge, Dein Lob, was au immer>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid, markdown=True)
# Die zu /gruppen gehï¿½renden Commands

            if (command[0] == "/gruppen"):
                bot.sende_nachricht("Ich kenne die folgenden Gruppen: \n Android-Hilfe: /granh \n Spamgruppe: /grspam \n Blackjackgruppe: /grbj", chatid, nachrichtid)

            if (command[0] == "/granh"):
                bot.sende_nachricht("Die inoffizielle Gruppe von http://www.android-hilfe.de, die Gruppe in der du ï¿½ber Android diskutieren kannst (und jeden Morgen ein nettes ''Guten Morgen zusammen'' von Mirko kriegst)! \n Rein kommst du mit diesem Link: [Android-Hilfe](https://telegram.me/androidhilfe)", chatid, nachrichtid, markdown=True)
            if (command[0] == "/grspam"):
                bot.sende_nachricht("Hier kannst du soviel Bots, Sticker und wasauchimmer spammen wie du willst! Komm einfach rein: [Spamshit](https://telegram.me/spamshit)", chatid, nachrichtid, markdown=True)
            if (command[0] == "/grbj"):
                bot.sende_nachricht("Eine kleine Gruppe, in der man mit dem @blackjackbot spielen kann! Kommt einfach rein: [Playblackjack](telegram.me/playblackjack)", chatid, nachrichtid, markdown=True)

            if (command[0] == "/gruppevorschlagen"):
                if (len(message) > 1):
                    words=len(message)
                    send = "Neuer Gruppenvorschlag von " + uservorname + " ID: " + str(userid) + "\n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, -151573627)
                    bot.sende_nachricht("Dein Vorschlag wurde versendet! Wir werden dich kontaktieren!", chatid, nachrichtid)
                else:
                    bot.sende_nachricht("Bitte schicke mir dieses Command so: \n /gruppevorschlagen `<Gruppenname und kurze Vorstellung der Gruppe>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid, markdown=True)
# Alles was mit Usergruppen zu tun hat
            if (command[0] == "/usergroup"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Du bist ein *globaler Admin*!", chatid, nachrichtid, markdown=True)
                elif (str(userid) in blacklist):
                    bot.sende_nachricht("Du bist *gebannt*!", chatid, nachrichtid, markdown=True)
                else:
                    bot.sende_nachricht("Du wurdest *nicht kategorisiert*!", chatid, nachrichtid, markdown=True)
# Admincommands
            if (command[0]== "/admincommands"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Admins können folgende Befehle verwenden:\n /reload - Den Bot neustarten \n /ban - Jemanden vom Bot bannen \n /send `<id> <nachricht>` - Eine Nachricht über den Bot versenden \n /addadmin - Jemanden zum globalen Admin machen", chatid, nachrichtid, markdown=True)
                    break
                else:
                    bot.sende_nachricht("Du kannst die Befehle für Admins nicht abrufen, da du kein *globaler Admin* bist!", chatid, nachrichtid, markdown=True)

            if (command[0] == "/ban"):
                if (str(userid) in admins):
                    if (str(answereduserid) in admins):
                        bot.sende_nachricht("Ein globaler Admin kann nicht vom Bot gebannt werden!", chatid, nachrichtid, markdown=True)
                        break
                    if (str(answereduserid) == '0'):
                        bot.sende_nachricht("*Ups*, hast du auf denjenigen geantwortet den du bannen willst?", chatid, nachrichtid, markdown=True)
                        break
                    if (str(answereduserid) not in blacklist):
                        blacklist.append(str(answereduserid))
                        with open("blacklist.txt", "a") as file:
                            newline = "\n" + str(answereduserid)
                            file.write(newline)
                            bot.sende_nachricht("User *" + str(answereduserid) + "* wurde vom Bot gebannt!", chatid, nachrichtid, markdown=True)
                        break
                    if (str(answereduserid) in blacklist):
                        bot.sende_nachricht("Der User ist bereits vom Bot gebannt!", chatid, nachrichtid, markdown=True)
                else:
                    alarm("*Jemanden mit /ban vom Bot bannen*")

            if (command[0] == "/addadmin"):
                if (str(userid) in admins):
                    if (str(answereduserid) in admins):
                        bot.sende_nachricht("User *" + str(answereduserid) + "* ist bereits Admin!", chatid, nachrichtid, markdown=True)
                        break
                    if (answered == "yes"):
                        bot.sende_nachricht("User *" + str(answereduserid) + "* wurde als Admin hinzugefügt!", chatid, nachrichtid, markdown=True)
                        admins.append(str(answereduserid))
                        with open("admins.txt", "a") as file:
                            newline = "\n" + str(answereduserid)
                            file.write(newline)
                    else:
                        bot.sende_nachricht("*Ups*, hast du auf denjenigen geantwortet den du zum globalen Admin machen willst?", chatid, nachrichtid, markdown=True)
                else:
                     alarm("*Jemanden mit /addadmin zum globalen Admin machen*")

            if (command[0] == "/reload"):
                if (str(userid) in admins):
                    print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "] Der Bot wurde von Admin " + uservorname + " neugestartet"))
                    bot.sende_nachricht("Der Bot wird jetzt neugestartet...", chatid, nachrichtid, markdown=True)
                    raise BotStop(uservorname)
                else:
                      alarm("*Bot mit /reload neustarten*")

            if (command[0] == "/send"):
                if (str(userid) in admins):
                    try:
                        words = len(message)
                        send = ("Hier ist eine Nachricht von " + uservorname + " aus dem Team. \n \n ")
                        for x in range(2, words):
                            send = send + message[x] + " "
                        bot.sende_nachricht(send, int(message[1]))
                        bot.sende_nachricht("Nachricht verschickt.", chatid)
                    except TypeError:
                        bot.sende_nachricht("Etwas stimmt mit der ID nicht.", chatid)
                    except:
                        bot.sende_nachricht("*Ups*, hast du die Nachricht so verschickt? \n /send `<id> <nachricht>`", chatid, markdown=True)
                else:
                    alarm("*Nutzen von /send ohne Admin*")

# Die zu /pictures gehï¿½renden Commands
            if (command[0] == "/pictures"):
                bot.sende_nachricht("Es gibt die folgenden Bilder: \n /icon - Das Profilbild des bots", chatid, nachrichtid)

            if (command[0] == "/icon"):
                bot.sende_bild("pictures/icon.jpg", chatid)
# Spaï¿½antworten
            command = command[0].lower()
            x = 0
            for dat in message:
                message[x] = dat.lower()
                x = x + 1
            if ("tobs" in message or "tobs" in command):
                bot.sende_nachricht("Tobs... Tobs ist toll! \nSo *richtig richtig* toll! ??", chatid, nachrichtid, markdown=True)
            if ("brawlbot" in message or "brawlbot" in command):
                bot.sende_nachricht("*IGITT!* Ich hasse _Lua_!", chatid, nachrichtid, markdown=True)
            if ("ayy" in message or "ayy" in command):
                 bot.sende_nachricht("lmao", chatid, nachrichtid)
            if ("lmao" in message or "lmao" in command):
                bot.sende_nachricht("ayy", chatid, nachrichtid)
            if ("rip" in message or "rip" in command):
                bot.sende_nachricht("rest in pieces", chatid, nachrichtid)
            if ("janisfelixbot" in message or "JanisFelixBot" in command):
                bot.sende_nachricht("Das bin ich!", chatid, nachrichtid)
