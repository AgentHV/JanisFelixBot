from chatter.telegramBot import TelegramBot
#Für code muss der API-Key eingesetzt werden
bot=TelegramBot("code")
bot.gehe_online()
while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        chatid=nachrichtraw.chat.id
        userid=nachrichtraw.sender
        if nachrichtraw.inhalt != None:
            nachricht=nachrichtraw.inhalt.split()
            if (nachricht[0]=="/start" or nachricht[0] == "/start@janisfelixexperimentebot"):
                bot.sende_nachricht("Hallo, ich bin der Janisfelixbot! Programmiert haben mich @flixlix und @sonixier mithilfe der vereinfachten Bot-API (https://github.com/tnstrssnr/telegram-chatter). Bitte denk daran, dass ich noch nicht 24/7 online und nur eine Beta bin!", chatid)
            if (nachricht[0] == "/id" or nachricht[0] == "/id@janisfelixexperimentebot"):
                send=("Chat-ID= "+ str(chatid) + "\n Deine ID: " + str(userid))
                bot.sende_nachricht(send, chatid)
            if (nachricht[0] == "/help" or nachricht[0] == "/help@janisfelixexperimentebot"):
                bot.sende_nachricht("Der JanisFelixBot kann folgende Befehle: /start - Zeigt eine kurze Startnachricht \n /help - Zeigt dir diese Nachricht \n /id - Gibt dir deine ID und die des Chats", chatid)
