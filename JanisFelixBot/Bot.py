import time
from chatter.telegramBot import TelegramBot
bot=TelegramBot("bot token einfügen")
bot.gehe_online()
otherbots = open("otherbots.txt").readlines()
admins = open("admins.txt").readlines()
blacklist = open("blacklist.txt")
for x in range(0,len(admins)) :
    admins[x] = admins[x].rstrip()
print(admins)
helptext = open("messages/help.txt").read()

def save():
    file = open("admins.txt", "w")
    for dat in admins:
        file.write(dat)
        file.write("\n")
    file.close()
    file = open("otherbots.txt", "w")
    for dat in otherbots:
        file.write(dat)
        file.write("\n")

def alarm(verstoss):
    send = ("Achtung! Der User " + str(uservorname) + " (" + str(userid) + ") hat versucht die folgende Sache zu machen: \n " + str(verstoss))
    bot.sende_nachricht(send, -151573627)
    print(send)


while (1):
    time.sleep(3)
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        uservorname=nachrichtraw.sender.vorname
        nachrichtid=nachrichtraw.id
        answereduserid=0
        try:
            answereduserid=nachrichtraw.antwort.sender.id
        except AttributeError:
            answered="no"
        else:
            answered="yes"

        if (nachrichtraw.inhalt != None and str(userid) not in blacklist):
            message=nachrichtraw.inhalt.split()
            nachricht=message[0].split("@")
            if (nachricht[0]=="/start"):
                bot.sende_nachricht("Hallo, ich bin der Janisfelixbot! Programmiert haben mich @flixlix und @sonixier mithilfe der vereinfachten Bot-API (https://github.com/tnstrssnr/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin!", chatid, nachrichtid)

            if (nachricht[0] == "/id"):
                send="Chat-ID= "+ str(chatid) + "\n Deine ID: " + str(userid)
                if (answered == "yes"):
                    send=send + "\n Die ID der Person, auf die du geantwortet hast:" + str(answereduserid)
                bot.sende_nachricht(send, chatid, nachrichtid)

            if (nachricht[0] == "/null"):
                bot.sende_nachricht("​", chatid)

            if (nachricht[0] == "/markdown"):
                bot.sende_nachricht("Es gibt die folgenden Formatierungen: *bold*_italic_`fixedsys`[Link](www.google.com)", chatid, nachrichtid)

            if (nachricht[0] == "/help"):
                bot.sende_nachricht(helptext, chatid, nachrichtid)

            if (nachricht[0] == "/send"):
                if (str(userid) in admins):
                    try:
                        bot.sende_nachricht("")
                    except:
                        bot.sende_nachricht("Ups, es ist ein Fehler aufgetreten! Bitte schick mir das Command so: \n /send <id> <text>")

#Spaßantworten
            if ("ayy" in message or "ayy" in nachricht):
                bot.sende_nachricht("lmao", chatid, nachrichtid)
            if ("lmao" in message or "lmao" in nachricht):
                bot.sende_nachricht("ayy", chatid, nachrichtid)
            if ("rip" in message or "rip" in nachricht):
                bot.sende_nachricht("rest in pieces", chatid, nachrichtid)
            if ("janisfelixbot" in message or "JanisFelixBot" in nachricht):
                bot.sende_nachricht("Das bin ich!", chatid, nachrichtid)
#Die zu /gruppen gehörenden Commands

            if (nachricht[0] == "/gruppen"):
                bot.sende_nachricht("Ich kenne die folgenden Gruppen: \n Android-Hilfe: /granh \n Spamgruppe: /grspam \n Blackjackgruppe: /grbj", chatid, nachrichtid)

            if (nachricht[0] == "/granh"):
                bot.sende_nachricht("Die inoffizielle Gruppe von http://www.android-hilfe.de, die Gruppe in der du über Android diskutieren kannst (und jeden Morgen ein nettes ''Guten Morgen zusammen'' von Mirko kriegst)! \n Rein kommst du mit diesem Link: [Link einfügen]", chatid, nachrichtid)
            if (nachricht[0] == "/grspam"):
                bot.sende_nachricht("Hier kannst du soviel Bots, Sticker und wasauchimmer spammen wie du willst! Komm einfach rein: https://telegram.me/spamshit", chatid, nachrichtid)
            if (nachricht[0] == "/grbj"):
                bot.sende_nachricht("Eine kleine Gruppe, in der man mit dem @blackjackbot spielen kann! Kommt einfach rein: telegram.me/playblackjack", chatid, nachrichtid)

            if (nachricht[0] == "/feedback"):
                if (len(message) > 1):
                    words=len(message)
                    send = "Ein feedback von " + uservorname + "(" + str(userid) + ") wurde gesendet. \n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, -151573627)
                else:
                    bot.sende_nachricht("Bitte schicke mir diesen Command so: \n /feedback <Deine Verbesserungsvorschläge> \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)

                      if (nachricht[0] == "/gruppevorschlagen"):
                if (len(message) > 1):
                    words=len(message)
                    send = "Neuer Gruppenvorschlag von " + uservorname + " ID: " + str(userid) + "\n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, -151573627)
                else:
                    bot.sende_nachricht("Bitte schicke mir dieses Command so: \n /gruppevorschlagen <Gruppenname und kurze Vorstellung der Gruppe> \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)

            if (nachricht[0] == "/stop"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Der Bot beendet sich jetzt!", chatid, nachrichtid)
                    raise
                else:
                      bot.sende_nachricht("Du bist kein Admin, Anzeige ist raus!", chatid, nachrichtid)
                      alarm("Bot mit /stop beenden")
# Alles was mit Usergruppen zu tun hat
            if (nachricht[0] == "/group"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Du bist ein globaler Admin!", chatid, nachrichtid)
                else:
                    bot.sende_nachricht("Du wurdest nicht kategorisiert!", chatid, nachrichtid)


