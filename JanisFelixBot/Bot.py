from chatter.telegramBot import TelegramBot
bot=TelegramBot("hier bot token einfügen")
while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        id=nachrichtraw.chat.id
        nachricht=nachrichtraw.inhalt.split()
        if (nachricht[0]=="/test"):
            bot.sende_nachricht("Juhu", id)
        if (nachricht[0] == "/id"):
            bot.sende_nachricht(str(id), id)
        if (nachricht[0] == "/help"
            bot.sende_nachricht("Der JanisFelixBot kann folgende Befehle:
                                /help /id")
                                
                                
