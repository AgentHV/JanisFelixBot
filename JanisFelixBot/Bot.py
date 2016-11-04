import time
from chatter.telegramBot import TelegramBot
bot=TelegramBot("token einfügen")
bot.gehe_online()
otherbots = open("otherbots.txt").readlines()
admins = open("admins.txt").readlines()
for x in range(0,len(admins)) :
    admins[x] = admins[x].rstrip()
    admins[x].replace("'", "")
print(admins)

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

while (1):
    time.sleep(2)
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        uservorname=nachrichtraw.sender.vorname
        if (userid in admins):
            admin = 1
        else:
            admin = 0
        if nachrichtraw.inhalt != None:
            message=nachrichtraw.inhalt.split()
            nachricht=message[0].split("@")
            if (nachricht[0]=="/start"):
                bot.sende_nachricht("Hallo, ich bin der Janisfelixbot! Programmiert haben mich @flixlix und @sonixier mithilfe der vereinfachten Bot-API (https://github.com/tnstrssnr/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin! Link zur Repository: https://github.com/Sonixier/JanisFelixBot", chatid)
            if (nachricht[0] == "/id"):
                send=("Chat-ID= "+ str(chatid) + "\n Deine ID: " + str(userid))
                bot.sende_nachricht(send, chatid)
            if (nachricht[0] == "/null"):
                bot.sende_nachricht("​", chatid)
            if (nachricht[0] == "/markdown"):
                bot.sende_nachricht("Es gibt die folgenden Formatierungen: *bold*_italic_`fixedsys`[Link](www.google.com)", chatid)
            if (nachricht[0] == "/help"):
                bot.sende_nachricht("Ich kann folgende Befehle: /start - Zeigt eine kurze Startnachricht \n /gruppen - Hier schlage ich dir ein paar Gruppen vor \n /gruppevorschlagen - Du hast eine eigene Gruppe oder kennst eine, die es verdient hat in meinen Vorschlägen zu erscheinen? Klick dieses Command an! \n /help - Zeigt dir diese Nachricht \n /id - Gibt dir deine ID und die des Chats", chatid)
            #Die zu /gruppen gehörenden Commands
            if (nachricht[0] == "/gruppen"):
                bot.sende_nachricht("Ich kenne die folgenden Gruppen: \n Android-Hilfe: /granh \n Spamgruppe: /grspam \n Blackjackgruppe: /grbj", chatid)
            if (nachricht[0] == "/granh"):
                bot.sende_nachricht("Die inoffizielle Gruppe von http://www.android-hilfe.de, die Gruppe in der du über Android diskutieren kannst (und jeden Morgen ein nettes ''Guten Morgen zusammen'' von Mirko kriegst)! \n Rein kommst du mit diesem Link: [Link einfügen]", chatid)
            if (nachricht[0] == "/grspam"):
                bot.sende_nachricht("Hier kannst du soviel Bots, Sticker und wasauchimmer spammen wie du willst! Komm einfach rein: https://telegram.me/spamshit", chatid)
            if (nachricht[0] == "/grbj"):
                bot.sende_nachricht("Eine kleine Gruppe, in der man mit dem @blackjackbot spielen kann! Kommt einfach rein: telegram.me/playblackjack", chatid)
            if (nachricht[0] == "/gruppevorschlagen"):
                if (len(message) > 1):
                    words=len(message)
                    send = "Neuer Gruppenvorschlag von " + uservorname + " ID: " + str(userid) + "\n"
                    for x in range(1, words):
                        send = send + message[x] + " "
                    bot.sende_nachricht(send, -151573627)
                else:
                    bot.sende_nachricht("Bitte schicke mir diesen Command so: \n /gruppevorschlagen <Gruppenname und kurze Vorstellung der Gruppe> \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid)
            if (nachricht[0] == "ayy"):
                    bot.sende_nachricht("lmao", chatid)
            if (nachricht[0] == "lmao"):
                    bot.sende_nachricht("ayy", chatid)
            if (nachricht[0] == "rip"):
                    bot.sende_nachricht("rest in pieces", chatid)
            if (nachricht[0] == "JanisFelixBot"):
                    bot.sende_nachricht("Das bin ich!", chatid)
# Alles was mit Usergruppen zu tun hat
            if (nachricht[0] == "/stop"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Der Bot beendet sich jetzt!", chatid)
                    raise
                else:
                    bot.sende_nachricht("Du bist kein Admin!", chatid)
            if (nachricht[0] == "/group"):
                if (str(userid) in admins):
                    bot.sende_nachricht("Du bist ein Admin!", chatid)
                else:
                    bot.sende_nachricht("Du wurdest nicht kategorisiert!", chatid)


