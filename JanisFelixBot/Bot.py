import time
from chatter.telegramBot import TelegramBot
#Für code muss dein API-Key vom BotFather eingesetzt werden
bot=TelegramBot("code")
bot.gehe_online()
while (1):
    time.sleep(2)
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender.id
        if nachrichtraw.inhalt != None:
            message=nachrichtraw.inhalt.split()
            nachricht=message[0].split("@")
            if (nachricht[0]=="/start"):
                bot.sende_nachricht("Hallo, ich bin der Janisfelixbot! Programmiert haben mich @flixlix und @sonixier mithilfe der vereinfachten Bot-API (https://github.com/tnstrssnr/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin!", chatid)
            if (nachricht[0] == "/id"):
                send=("Chat-ID= "+ str(chatid) + "\n Deine ID: " + str(userid))
                bot.sende_nachricht(send, chatid)
            if (nachricht[0] == "/help"):
                bot.sende_nachricht("Der JanisFelixBot kann folgende Befehle: /start - Zeigt eine kurze Startnachricht \n /help - Zeigt dir diese Nachricht \n /id - Gibt dir deine ID und die des Chats", chatid)
