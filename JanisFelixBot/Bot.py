from chatter.telegramBot import TelegramBot
#Für code muss der API-Key eingesetzt werden
bot=TelegramBot("code")
while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        if nachrichtraw.inhalt != None:
            nachricht=nachrichtraw.inhalt.split()
            if (nachricht[0]=="/start"):
                bot.sende_nachricht("Hallo, ich bin der Janisfelixbot! Programmiert haben mich @flixlix und @sonixier mithilfe der vereinfachten Bot-API (https://github.com/tnstrssnr/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin!", chatid)
            if (nachricht[0] == "/id"):
                send=("Chat-ID= "+ str(chatid))
                bot.sende_nachricht(send, chatid)
            if (nachricht[0] == "/help"):
                bot.sende_nachricht("Der JanisFelixBot kann folgende Befehle: /help /id", chatid)
        else:
            bot.sende_nachricht("Ein Fehler ist aufgetreten!")
