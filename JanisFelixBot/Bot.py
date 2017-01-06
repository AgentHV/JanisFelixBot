# JanisFelixBot - von Janis und Felix
# Die benötigten module:
import time
import os
import pyqrcode
import regex
from os.path import isfile
from telegraph import Telegraph
from chatter.telegramBot import TelegramBot
from cleverbot import Cleverbot
from pyshorteners import Shortener
from random import randint
bot=TelegramBot("telegram api key einfügen")
bot.gehe_online()
nachrichten = bot.hole_updates()
telegraph = Telegraph()
otherbots = open("otherbots.txt").readlines()
n=0
given = False
admins = open("admins.txt").readlines()
for x in admins:
    admins[n] = x.rstrip()
    n += 1
n = 0
bitusers = open("bits/users.txt").readlines()
for x in bitusers:
    bitusers[n] = int(x.rstrip())
    n += 1
blacklist = open("blacklist.txt").readlines()
helptext = open("messages/help.txt").read()
def alarm(verstoss):
    send = ("Achtung! Der User " + str(uservorname) + " (" + str(userid) + ") hat versucht die folgende Sache zu machen: \n " + str(verstoss))
    bot.sende_nachricht(send, -151573627)
    print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "]" + send))
    bot.sende_nachricht("Du bist kein Admin, Anzeige ist raus!", chatid, nachrichtid)
def setbits(bits, userid):
    filename = "bits/" + str(userid) + ".txt"
    if (isfile(filename)):
        dailybits = readdailybits(userid)
        with open(filename, 'w') as file:
            file.write(str(bits) + "\n" + dailybits)
    else:
        with open(filename, 'x') as file:
            file.write(str(bits))

def readbits(userid):
    filename = "bits/" + str(userid) + ".txt"
    with open(filename, 'r') as file:
        filecontent = file.readlines()
        return int(filecontent[0])

def setdailybits(bits, userid):
    filename = "bits/" + str(userid) + ".txt"
    if (isfile(filename)):
        oldbits = str(readbits(userid))
        with open(filename, 'w') as file:
            file.write(oldbits + "\n" + str(bits) + "\n" + uservorname)

def readdailybits(userid):
    filename = "bits/" + str(userid) + ".txt"
    with open(filename, 'r') as file:
        filecontent = file.readlines()
        return int(filecontent[1])

print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "] Der Bot wurde erfolgreich gestartet! Die IDs der Admins sind: " + str(admins) + "Die User der Bits sind:" + str(bitusers)))
while (1):
    if (time.localtime()[3] == 0 and not given):
        given = True
        for userid in bitusers:
            setbits(readbits(userid) + readdailybits(userid), userid)
    if (time.localtime()[3] > 0 and given):
        given = False

    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        uservorname=nachrichtraw.sender.vorname
        nachrichtid=nachrichtraw.id
        answereduserid=0
        if (nachrichtraw.antwort == None):
            answered=False
        else:
            answereduserid=nachrichtraw.antwort.sender.id
            answeredusername=nachrichtraw.antwort.sender.vorname
            answered=True
        if (nachrichtraw.inhalt != None and (str(userid) not in blacklist)):
            message = nachrichtraw.inhalt.split()
            command = message[0].split("@")
            if ((len(command) > 1 and command[1] == "JanisFelixBetaBot") or len (command) == 1):
                if (command[0]== "/start"):
                    bot.sende_nachricht("Hallo, ich bin der *Janisfelixbot*! Programmiert haben mich @flixlix und @sonixier mithilfe von [Felix's Fork der vereinfachten Bot-API](https://github.com/Flixlix/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin! Schreibe /help für eine Liste der Befehle.", chatid, nachrichtid)

                if (command[0] == "/id"):
                    send="Chat-ID: "+ str(chatid) + "\n Deine ID: " + str(userid) + "\n Vorname: " + str(uservorname)
                    if (answered == True):
                        send=send + "\n Die ID der Person, auf die du geantwortet hast:" + str(answereduserid)
                    bot.sende_nachricht(send, chatid, nachrichtid)

                if ("janisfelixbot" in message or "JanisFelixBot" in command):
                    if (len(message) > 1):
                        cb = Cleverbot()
                        cb.ask(" " + str(message) + " ")
                        cleverask = cb.ask(" " + str(message) + " ")
                        bot.sende_nachricht(cleverask, chatid, nachrichtid)
                if (command[0] == "/isup"):
                  if (len(message) > 1):
                    words = len(message)
                    for x in range(1, words):
                      hostname = message[x] 
                      response = os.system("ping -c 1 " + hostname)
                      if response == 0:
                         up = message[x] + " ist online!"
                         bot.sende_nachricht(up, chatid, nachrichtid)
                      else:
                         down = message[x] + " ist offline oder dies ist keine Webadresse."
                         bot.sende_nachricht(down, chatid, nachrichtid)
                  else:
                      bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: /isup `<Dein Link>` ", chatid, nachrichtid)
                if (command[0] == "/null"):
                    bot.sende_nachricht(" ", chatid)
                if (command[0] == "/echo"):
                    if (len(message) > 1):
                        words = len(message)
                        send = "*" + uservorname + " sagt:* \n \n"
                        for x in range(1, words):
                            send = send + message[x] + " "
                        bot.sende_nachricht(send, chatid)
                    else:
                        bot.sende_nachricht(
                            "Bitte schicke mir diesen Command so: \n /echo `<Dein Text>` \n Gibt deinen Text aus. *Markdown* wird unterstützt!", chatid, nachrichtid)

                if (command[0] == "/markdown"):
                    bot.sende_nachricht("Es gibt die folgenden Formatierungen: \n//*bold//*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk)", chatid, nachrichtid)
                    bot.sende_nachricht("Diese sind wie folgt anzuwenden: \n*bold*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk)", chatid, nachrichtid)

                if (command[0] == "/time"):
                    datum = str(time.strftime("%d.%m.%Y"))
                    zeit = str(time.strftime(" %H:%M:%S"))
                    bot.sende_nachricht("Datum: " + str(datum) + "\nUhrzeit:" + str(zeit), chatid, nachrichtid)

                if (command[0] == "/short"):
                  if (len(message) > 1):
                     words = len(message)
                     for x in range(1, words):
                       try:
                          url = message[x]
                          api_key = "goo.gl api key einfügen"
                          shortener = Shortener("Google", api_key=api_key)
                          bot.sende_nachricht("Der gekürtzte Link lautet: {}".format(shortener.short(url)), chatid, nachrichtid)
                       except ValueError:
                          bot.sende_nachricht("*Ups*, `" + url + "` ist keine Internetadresse. Bitte beachte das http:// bzw. https:// im Link stehen muss.", chatid, nachrichtid)
                  else:
                      bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: /short `<Dein Link>`", chatid, nachrichtid)
                if (command[0] == "/qrgen"):
                    if (len(message) > 1):
                        words = len(message)
                        qr = pyqrcode.create(message[x])
                        qr.png("qrcode.png", scale=20)
                        bot.sende_bild("qrcode.png", chatid)
                        os.remove("qrcode.png")
                if (command[0] == "/telegraph"):
                    if (len(message) > 1):
                        words = len(message)
                        for x in range(1, words):
                            tgmsg = message
                            sendtgmsg = ' '.join(tgmsg)
                        newtgmsg = sendtgmsg.replace("/telegraph", "")
                        newtgmsg = newtgmsg + "\n\nDieses Telegraph wurde mit JanisFelixBot (t.me/Janis_Felix_Bot) erstellt."
                        telegraph.create_account(short_name=uservorname)
                        response = telegraph.create_page(uservorname + " (" + str(userid) + ") Telegraph",
                                                         html_content='<p>' + str(newtgmsg) + '</p>')
                    telegraphmsg = "http://telegra.ph/{}".format(response["path"])
                    bot.sende_nachricht(telegraphmsg, chatid)
                if (command[0] == "/random"):
                    if (len(message) > 1):
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
                                send = " " + str(uservorname) + " ? "
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
                        bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: /random `<Dein Objekt/Person...>`", chatid)
                if (command[0] == "/help"):
                    if str(userid) in admins:
                       adminhelp = helptext + "\n/admincommands - Sende commands für Admins"
                       bot.sende_nachricht(adminhelp, chatid, nachrichtid)
                       break
                    else:
                        bot.sende_nachricht(helptext, chatid, nachrichtid)
                if (command[0] == "/tl"):
                    if (len(message) > 1):
                        words = len(message)
                        for x in range(2, words):
                            print(message[x])
                        gs = goslate.Goslate()
                        tltext = (gs.translate("hallo", "en"))
                    else:
                        bot.sende_nachricht("Blablablubb", chatid, nachrichtid)

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
                            "Bitte schicke mir diesen Command so: \n /feedback `<Deine VerbesserungsvorschlÃ¤ge, Dein Lob, was au immer>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)
    # Die zu /gruppen gehörenden Commands

                if (command[0] == "/gruppen"):
                    bot.sende_nachricht("Ich kenne die folgenden Gruppen: \n Android-Hilfe: /granh \n Spamgruppe: /grspam \n Blackjackgruppe: /grbj", chatid, nachrichtid)

                if (command[0] == "/granh"):
                    bot.sende_nachricht("Die inoffizielle Gruppe von http://www.android-hilfe.de, die Gruppe in der du über Android diskutieren kannst (und jeden Morgen ein nettes ''Guten Morgen zusammen'' von Mirko kriegst)! \n Rein kommst du mit diesem Link: [Android-Hilfe](https://telegram.me/androidhilfe)", chatid, nachrichtid)
                if (command[0] == "/grspam"):
                    bot.sende_nachricht("Hier kannst du soviel Bots, Sticker und wasauchimmer spammen wie du willst! Komm einfach rein: [Spamshit](https://telegram.me/spamshit)", chatid, nachrichtid)
                if (command[0] == "/grbj"):
                    bot.sende_nachricht("Eine kleine Gruppe, in der man mit dem @blackjackbot spielen kann! Kommt einfach rein: [Playblackjack](telegram.me/playblackjack)", chatid, nachrichtid)

                if (command[0] == "/gruppevorschlagen"):
                    if (len(message) > 1):
                        words=len(message)
                        send = "Neuer Gruppenvorschlag von " + uservorname + " ID: " + str(userid) + "\n"
                        for x in range(1, words):
                            send = send + message[x] + " "
                        bot.sende_nachricht(send, -151573627)
                        bot.sende_nachricht("Dein Vorschlag wurde versendet! Wir werden dich kontaktieren!", chatid, nachrichtid)
                    else:
                        bot.sende_nachricht("Bitte schicke mir dieses Command so: \n /gruppevorschlagen `<Gruppenname und kurze Vorstellung der Gruppe>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)
    # Alles was mit Usergruppen zu tun hat
                if (command[0] == "/usergroup"):
                    if (str(userid) in admins):
                        bot.sende_nachricht("Du bist ein *globaler Admin*!", chatid, nachrichtid)
                    elif (str(userid) in blacklist):
                        bot.sende_nachricht("Du bist *gebannt*!", chatid, nachrichtid)
                    else:
                        bot.sende_nachricht("Du wurdest *nicht kategorisiert*!", chatid, nachrichtid)
    #Die Bits (B)
                if (command[0] == "/bits"):
                    filename = "bits/" + str(userid) + ".txt"
                    if (userid in bitusers):
                        bot.sende_nachricht(("Hallo " + str(uservorname) + "! Dein aktueller Kontostand ist `" + str(readbits(userid)) + "` Bits. Du bekommst jeden Tag `" + str(readdailybits(userid)) + "` Bits.\nDu kannst folgende Befehle benutzen:\n/givebits <Anzahl der zu überweisenden Bits> Bitte denke daran, auf die Person der du Bits schicken willst zu antworten."), chatid)
                    else:
                        bot.sende_nachricht("Hallo " + str(uservorname) + "! Nutze /bitsreg um dir ein BitKonto anzulegen und diesen Service nutzen zu können!", chatid)
                if (command[0] == "/givebits"):
                    if (answered==True and len(message) > 1):
                        if (message[1].isdigit()):
                            with open("bits/logs.txt", 'a') as log:
                                log.write("Überweisung: " + answeredusername + " (" + str(answereduserid) + ") hat " + message[1] + "von " + uservorname + " (" + str(userid) + ") bekommen.")
                                if (readbits(userid) > int(message[1])):
                                    if answereduserid in bitusers:
                                        if userid in bitusers:
                                            setbits(readbits(userid) - int(message[1]), userid)
                                            setbits(readbits(answereduserid) + int(message[1]), answereduserid)
                                            log.write("Überweisung durchgeführt!")
                                            bot.sende_nachricht("Deine Überweisung von `" + message[1] + "` B an " + answeredusername + " wurde durchgeführt. Du hast jetzt noch `" + str(readbits(userid)) + "` B.", chatid)
                                            bot.sende_nachricht(uservorname + " hat dir `" + str(message[1]) + "` Bits geschickt. Dank ihm/ihr hast du jetzt `" + str(readbits(answereduserid)) + "` B.", answereduserid)
                                        else:
                                            bot.sende_nachricht("Du hast kein Bitkonto!", chatid)
                                    else:
                                        bot.sende_nachricht(answeredusername + " hat kein Bitkonto!", chatid)
                                else:
                                    bot.sende_nachricht("Du hast nicht genug B!", chatid)
                        else:
                            bot.sende_nachricht("Bitte antworte auf jemanden, wenn du mir dieses Command sendest. Ausserdem muss nach /givebits die Anzahl der zu überweisenden Bits stehen.", chatid)
                    else:
                        bot.sende_nachricht("Bitte antworte auf jemanden, wenn du mir dieses Command sendest. Ausserdem muss nach /givebits die Anzahl der zu überweisenden Bits stehen.", chatid)
                if (command[0] == "/bitsreg"):
                    filename = "bits/" + str(userid) + ".txt"
                    if (not isfile(filename)):
                        setbits(1000, userid)
                        setdailybits(100, userid)
                        with open("bits/users.txt", 'a') as file:
                            file.write("\n" + userid)
                            bitusers.append(userid)
                        bot.sende_nachricht("Dein BitKonto wurde angelegt! Du hast `1000` B Startkapital. Nutze /bits um anzufangen. Tipp: Starte den Bot privat, um dieses Feature bestmöglich nutzen zu können.\nBitte beachte, dass alle Zahlungen geloggt werden!", chatid)
                    else:
                        bot.sende_nachricht("Du hast bereits ein BitKonto. Wenn du es neu anlegen lassen möchtest, kontaktiere bitte @flixlix oder @sonixier!", chatid)
                if (command[0] == "/delbitkonto"):
                    if (str(userid) in admins):
                        if (str(answereduserid) == '0'):
                            bot.sende_nachricht("Bitte antworte auf die Person von der du das BitKonto löschen willst.", chatid)
                            break
                        filename = "bits/" + str(answereduserid) + ".txt"
                        if (userid in bitusers):
                            os.remove(filename)
                            bitusers.remove(userid)
                            with open("bits/users.txt", 'w') as file:
                                for userid in bitusers:
                                    file.write(userid + "\n")
                            bot.sende_nachricht("Das Konto der ID "+ str(answereduserid) + " wurde gelöscht.", chatid)
                            break
                        if not (isfile(filename)):
                            bot.sende_nachricht("Dieser User hat kein BitKonto.", chatid)
                            break
                    else:
                        bot.sende_nachricht("Du bist kein globaler Admin!", chatid)
                        break
    # Admincommands
                if (command[0]== "/admincommands"):
                    if (str(userid) in admins):
                        bot.sende_nachricht("Admins können folgende Befehle verwenden:\n /reload - Den Bot neustarten \n /ban - Jemanden vom Bot bannen \n /send `<id> <nachricht>` - Eine Nachricht über den Bot versenden \n /addadmin - Jemanden zum globalen Admin machen \n /delbitkonto - Das BitKonto von jemandem löschen", chatid, nachrichtid)
                        break
                    else:
                        bot.sende_nachricht("Du kannst die Befehle für Admins nicht abrufen, da du kein *globaler Admin* bist!", chatid, nachrichtid)

                if (command[0] == "/ban"):
                    if (str(userid) in admins):
                        if (str(answereduserid) in admins):
                            bot.sende_nachricht("Ein globaler Admin kann nicht vom Bot gebannt werden!", chatid, nachrichtid)
                            break
                        if (str(answereduserid) == '0'):
                            bot.sende_nachricht("*Ups*, hast du auf denjenigen geantwortet den du bannen willst?", chatid, nachrichtid)
                            break
                        if (str(answereduserid) not in blacklist):
                            blacklist.append(str(answereduserid))
                            with open("blacklist.txt", "a") as file:
                                newline = "\n" + str(answereduserid)
                                file.write(newline)
                                bot.sende_nachricht("User *" + str(answereduserid) + "* wurde vom Bot gebannt!", chatid, nachrichtid)
                            break
                        if (str(answereduserid) in blacklist):
                            bot.sende_nachricht("Der User ist bereits vom Bot gebannt!", chatid, nachrichtid)
                    else:
                        alarm("*Jemanden mit /ban vom Bot bannen*")

                if (command[0] == "/addadmin"):
                    if (str(userid) in admins):
                        if (str(answereduserid) in admins):
                            bot.sende_nachricht("User *" + str(answereduserid) + "* ist bereits Admin!", chatid, nachrichtid)
                        elif (answered == True):
                            bot.sende_nachricht("User *" + str(answereduserid) + "* wurde als Admin hinzugefügt!", chatid, nachrichtid)
                            admins.append(str(answereduserid))
                            with open("admins.txt", "a") as file:
                                newline = "\n" + str(answereduserid)
                                file.write(newline)
                        else:
                            bot.sende_nachricht("*Ups*, hast du auf denjenigen geantwortet den du zum globalen Admin machen willst?", chatid, nachrichtid)
                    else:
                         alarm("*Jemanden mit /addadmin zum globalen Admin machen*")

                if (command[0] == "/reload"):
                    if (str(userid) in admins):
                        print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "] Der Bot wurde von Admin " + uservorname + " neugestartet"))
                        bot.sende_nachricht("Der Bot wird jetzt neugestartet...", chatid, nachrichtid)
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
                            bot.sende_nachricht("*Ups*, hast du die Nachricht so verschickt? \n `/send <id> <nachricht>`", chatid)
                    else:
                        alarm("*Nutzen von /send ohne Admin*")

    # Die zu /pictures gehörenden Commands
                if (command[0] == "/pictures"):
                    bot.sende_nachricht("Es gibt die folgenden Bilder: \n /icon - Das Profilbild des bots", chatid, nachrichtid)

                if (command[0] == "/icon"):
                    bot.sende_bild("pictures/icon.jpg", chatid)

    # Spaßantworten
                x = 0
                for dat in message:
                    message[x] = dat.lower()
                    x = x + 1
                x = 0
                for dat in command:
                    command[x] = dat.lower()
                    x = x + 1
                if ("tobs" in message or "tobs" in command):
                    bot.sende_nachricht("Tobs... Tobs ist toll! \nSo *richtig richtig* toll!❤️", chatid, nachrichtid)
