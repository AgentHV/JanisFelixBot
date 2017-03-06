# JanisFelixBot - von Janis und Felix
from chatter.telegramBot import TelegramBot
#----------------------------WICHTIG-------------------------------
# Bitte ersetze folgende Werte durch deine:
bot = TelegramBot("")
api_key = ""
admingroup = 
#----------------------------WICHTIG-------------------------------
# Die benötigten module:
import json
import urllib.request
import time
import os
import pyqrcode
import regex
import shutil
import wikipedia
from os.path import isfile
from telegraph import Telegraph
from cleverbot import Cleverbot
from random import randint
wikipedia.set_lang("de")
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
blacklist = open("blacklist.txt").readlines()
helptext = open("messages/help.txt").read()
def alarm(verstoss):
    send = ("Achtung! Der User " + str(uservorname) + " (" + str(userid) + ") hat versucht die folgende Sache zu machen: \n " + str(verstoss))
    bot.sende_nachricht(send, admingroup)
    print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "]" + send))
    bot.sende_nachricht("Du bist kein Admin, Anzeige ist raus!", chatid, nachrichtid)

print("[" + str(time.strftime("%d.%m.%Y %H:%M") + "] Der Bot wurde erfolgreich gestartet! Die IDs der Admins sind: " + str(admins)))
while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        uservorname=nachrichtraw.sender.vorname
        usernachname = nachrichtraw.sender.nachname
        username = nachrichtraw.sender.username
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
                afkusers = open("afkusers.txt").readlines()
                print(userid)
                print(afkusers)
                #if (str(userid) in str(afkusers)):
                    #print("wieder da")
                    #afkusers.replace(userid, "")
                    #bot.sende_nachricht(str(uservorname) + " ist wieder da.", chatid)
                if (command[0]== "/start"):
                    bot.sende_nachricht("Hallo, ich bin der *Janisfelixbot*! Programmiert haben mich @ChisanaNekoFlix und @sonixier mithilfe von [Felix's Fork der vereinfachten Bot-API](https://github.com/Flixlix/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin! Schreibe /help für eine Liste der Befehle.", chatid, nachrichtid)
                if (command[0]== "/afk"):
                    if (len(message) > 1):
                       words = len(message)
                       afkgrund = " "
                       for x in range(1, words):
                          afkgrund = afkgrund + message[x] + " "
                       bot.sende_nachricht(uservorname + " ist nun afk. (" + afkgrund + ")", chatid)
                    else:
                       bot.sende_nachricht(uservorname + " ist nun afk.", chatid, nachrichtid)
                    afkusers.append(str(userid))
                    with open("afkusers.txt", "a") as file:
                         newline = " \n " + str(userid)
                         file.write(newline)
                    print("nun afk")
                if (command[0]== "/about"):
                    bot.sende_nachricht("[JANISFELIXBOT](t.me/janis_felix_bot)\nmade with ❤️by [Janis](t.me/sonixier) & [Felix](t.me/ChisanaNekoFlix)\n\n[Den Bot im SoreBot bewerten](https://telegram.me/storebot?start=janis_felix_bot)\n[Github](https://github.com/Sonixier/JanisFelixBot)\n[Webseite](https://janisfelixbot.tk/)\n[vereinfachte Bot-API](https://github.com/Flixlix/telegram-chatter)", chatid)
                if (command[0] == "/btc"):
                    with urllib.request.urlopen('https://blockchain.info/de/ticker') as response:
                        html = response.read().decode()
                    btcdictionary = json.loads(html)
                    eurbtc = btcdictionary['EUR']['last']
                    usdbtc = btcdictionary['USD']['last']
                    sendmsg = "Ein Bitcoin entspricht " + str(eurbtc) + " € oder auch " + str(usdbtc) + "$. \nWir nutzen für diesen Service die [API von blockchain.info](https://blockchain.info/de/api/exchange_rates_api)"
                    bot.sende_nachricht(sendmsg, chatid)
                if (command[0] == "/id"):
                    send="Chat-ID: "+ str(chatid) + "\nDeine ID: " + str(userid) + "\nName: " + str(uservorname) + " " + str(usernachname) + "\nUsername: " + str(username)
                    if (answered == True):
                        send=send + "\n Die ID der Person, auf die du geantwortet hast: " + str(answereduserid)
                    bot.sende_nachricht(send, chatid, nachrichtid)

                #if (command[0] == '/ban'):
                    #if(bot.request("getChatMemeber?chat_id=" + chatid + userid['status']) == 'creator' or bot.request("getChatMemeber?chat_id=" + chatid + "&user_id=" + userid['status'] == 'administrator'):
                        #bot.ban(answereduserid, chatid)
                        #bot.sende_nachricht("Gebannt!", chatid, antwort_id=nachrichtid)
                    #else:
                        #bot.sende_nachricht("Du Schlingel willst jemanden bannen, obwohl du kein Admin bist? Tss tss tss...", chatid, antwort_id=userid)

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
                      bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: */isup* `<Dein Link>` ", chatid, nachrichtid)
                if (command[0] == "/null"):
                    bot.sende_nachricht(" ​", chatid)
                if (command[0] == "/echo"):
                    if (len(message) > 1):
                        words = len(message)
                        send = "*" + uservorname + " sagt:* \n \n"
                        for x in range(1, words):
                            send = send + message[x] + " "
                        bot.sende_nachricht(send, chatid)
                    else:
                        bot.sende_nachricht(
                            "Bitte schicke mir diesen Command so: \n */echo* `<Dein Text>` \n Gibt deinen Text aus. *Markdown* wird unterstützt!", chatid, nachrichtid)

                if (command[0] == "/markdown"):
                    bot.sende_nachricht("Es gibt die folgenden Formatierungen: \n*bold*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk)", chatid, nachrichtid)
                    bot.sende_nachricht("Diese sind wie folgt anzuwenden: \n*bold*\n _italic_\n `fixedsys`\n [Link](www.janisfelixbot.tk\nBitte bedenke, dass nur Bots Links verschicken können. Um das zu umgehen, empfehlen wir dir, @bold zu verwenden.)", chatid, nachrichtid, markdown=False)

                if (command[0] == "/time"):
                    datum = str(time.strftime("%d.%m.%Y"))
                    zeit = str(time.strftime(" %H:%M:%S"))
                    bot.sende_nachricht("Datum: " + str(datum) + "\nUhrzeit:" + str(zeit), chatid, nachrichtid)
                if (command[0] == "/wiki"):
                  if (len(message) > 1):
                      try:
                          words = len(message)
                          for x in range(1, words):
                              tgmsg = message
                              sendtgmsg = ' '.join(tgmsg)
                          newtgmsg = sendtgmsg.replace("/wiki", "")
                          wiki = wikipedia.page(newtgmsg)
                          url = wiki.url
                          titel = "*" + wiki.title + "*"
                          diekomplettewikimsg = titel + "\n" + wikipedia.summary(newtgmsg, sentences=3) + "\n[Artikel aufrufen](" + url + ")"
                          bot.sende_nachricht(diekomplettewikimsg, chatid, nachrichtid)
                      except wikipedia.exceptions.DisambiguationError:
                          bot.sende_nachricht("Es existieren mehrere Seiten mit diesem Titel. Bitte benutze einen anderen Suchbegriff.", chatid, nachrichtid)
                      except wikipedia.exceptions.PageError:
                          bot.sende_nachricht("Unter dem Suchbegriff wurde kein Artikel gefunden.", chatid, nachrichtid)
                      except wikipedia.exceptions.HTTPTimeoutError:
                          bot.sende_nachricht("Keine Antwort vom Server. Vielleicht ist Wikipedia offline? Probiere mal `/isup https://www.wikipedia.org`", chatid, nachrichtid)
                          bot.sende_nachricht("*Ein Fehler ist aufgetreten!*\nCommand: " + sendtgmsg + "\nFehler:HTTPTimeoutError\nKeine Antwort vom Server. Vielleicht ist Wikipedia offline?", admingroup)
                      except wikipedia.exceptions.WikipediaException:
                          bot.sende_nachricht("Ein Fehler ist aufgetreten. Bitte versuche es nocheinmal.", chatid, nachrichtid)
                          bot.sende_nachricht("*Ein Fehler ist aufgetreten!*\nCommand: " + sendtgmsg + "\nFehler:WikipediaException\nEin Fehler ist aufgetreten.", admingroup)
                      except wikipedia.exceptions.RedirectError:
                          bot.sende_nachricht("Unerwartet auf eine andere Seite weitergeleitet. Vielleicht ist der Artikel ein Platzhalter?", chatid, nachrichtid)
                      except ValueError:
                          bot.sende_nachricht("Ein Fehler ist aufgetreten.", chatid, nachrichtid)
                          bot.sende_nachricht("*Ein Fehler ist aufgetreten!*\nCommand: " + sendtgmsg + "\nFehler:ValueError\nStimmt etwas nicht mit den Wörtern im command nicht?", admingroup)
                  else:
                      bot.sende_nachricht("*Ups*, bitte schicke mir diesen Command so: */wiki* `<Dein Suchbegriff>`", chatid, nachrichtid)
                if (command[0] == "/short"):
                    if (len(message) == 2):
                        with urllib.request.urlopen('https://api-ssl.bitly.com/v3/shorten?longUrl='+message[1]+'&access_token=6e9523c8866cdb7b1d2bd9d281d858c5751d7324') as response:
                            html = response.read().decode()
                        bitly = json.loads(html)
                        if ('status_txt' in bitly and bitly['status_txt'] == "OK"):
                            shortenurl = bitly['data']['url'].replace("\/", "")
                            shortenurl = shortenurl.replace("http:", "")
                            bot.sende_nachricht("Die gekürzte URL lautet:\n" + shortenurl, chatid, nachrichtid)
                        else:
                            bot.sende_nachricht("Ups, `" + message[1] + "` ist keine Internetadresse oder irgendetwas ist schiefgegangen. Bitte beachte dass http:// bzw. https:// im Link stehen muss. Wenn du dir sicher bist, alles richtig gemacht zu haben, versuch es später einfach nochmal.", chatid, nachrichtid)
                    else:
                        bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: */short* `<Dein Link>`", chatid, nachrichtid)
                if (command[0] == "/qrgen"):
                    if (len(message) > 1):
                        try:
                           words = len(message)
                           qrtext = "\n"
                           for x in range(1, words):
                               qrtext = qrtext + message[x] + " "
                           qrtext = qrtext[:-1]
                           qrtext = qrtext.lstrip()
                           qrlink = "http://api.qrserver.com/v1/create-qr-code/?data=" + qrtext + "&size=512x512"
                           print(qrlink)
                           with urllib.request.urlopen(qrlink) as response, open("qrcode.png", 'wb') as out_file:
                               shutil.copyfileobj(response, out_file)
                           bot.sende_bild("qrcode.png", chatid)
                           os.remove("qrcode.png")
                        except:
                           bot.sende_nachricht("Ein Fehler ist aufgetreten. Bitte achte darauf kein *ä*, *ö* oder *ü* oder Sonderzeichen zu verwenden.", chatid)
                if (command[0] == "/telegraph"):
                    if (len(message) > 1):
                        words = len(message)
                        for x in range(1, words):
                            tgmsg = message
                            sendtgmsg = ' '.join(tgmsg)
                        newtgmsg = sendtgmsg.replace("/telegraph", "")
                        telegraph.create_account(short_name=uservorname)
                        response = telegraph.create_page(uservorname + " (" + str(userid) + ") Telegraph",
                                                         html_content='<p>' + str(newtgmsg) + '</p>')
                        telegraphmsg = "http://telegra.ph/{}".format(response["path"])
                        bot.sende_nachricht(telegraphmsg, chatid, nachrichtid)
                    else:
                        bot.sende_nachricht("Ups, bitte schicke mir diesen command so: */telegraph* `<Dein Text>`", chatid, nachrichtid, markdown=True)
                if (command[0] == "/random"):
                    if (len(message) > 1):
                        randomzahl = randint(0, 6)
                        if randomzahl == 0:
                                words = len(message)
                                send = " " + str(uservorname) + " gibt "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + " einen Keks."
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 1:
                                words = len(message)
                                send = " " + str(uservorname) + " ? "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + "!"
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 2:
                                words = len(message)
                                send = " "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + " liebt Lua."
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 3:
                                words = len(message)
                                send = " "
                                send = send + str(uservorname) + " küsst "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + " leidenschaftlich."
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 4:
                                words = len(message)
                                send = " "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + " mag TouchWiz. "
                                send = send + str(uservorname) + " hingegen versucht ihm CyanogenMod aufzuquatschen."
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 5:
                                words = len(message)
                                send = " "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + " ist ein typischer Fall von einem gerissenen Kondom."
                                bot.sende_nachricht(send, chatid)
                                break
                        if randomzahl == 6:
                                words = len(message)
                                send = "Sag "
                                send = send + nachrichtraw.inhalt.replace(message[0], '') + ", es soll sich verstecken. Die Müllabfuhr kommt!"
                                bot.sende_nachricht(send, chatid)
                                break
                    else:
                        bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so: */random* `<Dein Objekt/Person...>`", chatid)
                if (command[0] == "/help"):
                    if str(userid) in admins:
                       adminhelp = helptext + "\n/admincommands - Sende commands für Admins"
                       bot.sende_nachricht(adminhelp, chatid, nachrichtid)
                       break
                    else:
                        bot.sende_nachricht(helptext, chatid, nachrichtid)

                if (command[0] == "/feedback"):
                    if (len(message) > 1):
                        words = len(message)
                        send = "Ein feedback von " + uservorname + "(" + str(userid) + ") wurde gesendet. \n"
                        for x in range(1, words):
                            send = send + message[x] + " "
                        bot.sende_nachricht(send, admingroup)
                        bot.sende_nachricht("Dein Feedback wurde versendet! Wir werden dich kontaktieren!", chatid)
                    else:
                        bot.sende_nachricht(
                            "Bitte schicke mir diesen Command so: \n */feedback* `<Deine Verbesserungsvorschläge, Dein Lob, was au immer>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)
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
                        bot.sende_nachricht("Bitte schicke mir dieses Command so: \n */gruppevorschlagen* `<Gruppenname und kurze Vorstellung der Gruppe>` \n Wir werden dich dann kontaktieren. Bitte denke jedoch daran wenn du rumspammst, dass du dann einen Ban kassieren kannst!", chatid, nachrichtid)
    # Alles was mit Usergruppen zu tun hat
                if (command[0] == "/usergroup"):
                    if (str(userid) in admins):
                        bot.sende_nachricht("Du bist ein *globaler Admin*!", chatid, nachrichtid)
                    elif (str(userid) in blacklist):
                        bot.sende_nachricht("Du bist *gebannt*!", chatid, nachrichtid)
                    else:
                        bot.sende_nachricht("Du wurdest *nicht kategorisiert*!", chatid, nachrichtid)

    # Admincommands
                if (command[0]== "/admincommands"):
                    if (str(userid) in admins):
                        bot.sende_nachricht("Admins können folgende Befehle verwenden:\n /reload - Den Bot neustarten \n /ban - Jemanden vom Bot bannen \n /send `<id> <nachricht>` - Eine Nachricht über den Bot versenden \n /addadmin - Jemanden zum globalen Admin machen \n /delbitkonto - Das BitKonto von jemandem löschen", chatid, nachrichtid)
                        break
                    else:
                        bot.sende_nachricht("Du kannst die Befehle für Admins nicht abrufen, da du kein *globaler Admin* bist!", chatid, nachrichtid)

                if (command[0] == "/botban"):
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
                        alarm("*Jemanden mit /botban vom Bot bannen*")

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
                        raise "reload"
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
                            bot.sende_nachricht("*Ups*, hast du die Nachricht so verschickt? \n */send* `<id> <nachricht>`", chatid)
                    else:
                        alarm("*Nutzen von /send ohne Admin*")

    # Die zu /pictures gehörenden Commands
                if (command[0] == "/pictures"):
                    bot.sende_nachricht("Es gibt die folgenden Bilder:\n/icon - Das Profilbild des bots\n/cats - Katzenbilder\n/doge - Erstelle ein Doge-Meme mit deinem Text", chatid, nachrichtid)
                if (command[0] == "/icon"):
                    bot.sende_bild("pictures/icon.jpg", chatid)
                if (command[0] == "/doge"):
                    if (len(message) > 1):
                        try:
                           sendtgmsg = ' '.join(message)
                           print(sendtgmsg)
                           newtgmsg = sendtgmsg.replace("/doge", "")
                           print(newtgmsg)
                           doge = newtgmsg.replace(" ", "")
                           doge2 = doge.replace(";", "/")
                           doglink = "http://dogr.io/" + doge2 + ".png"
                           dogeimage = "doge.png"
                           print(doglink)
                           with urllib.request.urlopen(doglink) as response, open(dogeimage, 'wb') as out_file:
                               shutil.copyfileobj(response, out_file)
                           bot.sende_bild(dogeimage, chatid)
                           bot.sende_nachricht("Dies ist eine beta und noch nicht gänzlich ausgereift. Wenn du nur ein leeres Bild oder den Text\n`wow\nvery error parsing\nsuch sorry`\nerhältst, leite diese Nachricht bitte an einen meiner Entwickler weiter.\n\n*" + doglink + "\n" + doge2 + "*", chatid)
                           os.remove("doge.png")
                        except:
                           bot.sende_nachricht("Ein Fehler ist aufgetreten. Bitte achte darauf kein *ä*, *ö* oder *ü* oder Sonderzeichen zu verwenden.", chatid)
                    else:
                        bot.sende_nachricht("*Ups*, bitte schicke mir diesen command so:\n*/doge* `<erste Zeile/zweite Zeile/dritte Zeile...>`\nTrenne Zeilen mit einem /. Bitte beachte das dies eine Beta ist!",chatid)
                if (command[0] == "/cats"):
                   catszahl = randint(0, 2)
                   if catszahl == 0:
                      format = "gif"
                   if catszahl == 1:
                      format = "png"
                   if catszahl == 2:
                      format = "jpg"
                   catname = "cat." + str(format)
                   catlink = "http://thecatapi.com/api/images/get?format=src&type=" + format
                   with urllib.request.urlopen(catlink) as response, open(catname, 'wb') as out_file:
                       shutil.copyfileobj(response, out_file)
                   bot.sende_bild(catname, chatid)
                   os.remove(catname)

    # Spaßantworten
                x = 0
                for dat in message:
                    message[x] = dat.lower()
                    x += 1
                x = 0
                for dat in command:
                    command[x] = dat.lower()
                    x +=1
