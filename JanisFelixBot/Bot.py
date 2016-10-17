from chatter.telegramBot import TelegramBot
bot=TelegramBot("257382012:AAHNiJsoi8kO3r5TxYLseMh3lMYEH-Kf6bM")
while (1):
    nachrichten = bot.hole_updates()
    for nachrichtraw in nachrichten:
        id=nachrichtraw.chat.id
        nachricht=nachrichtraw.inhalt.split()
        if (nachricht[0]=="/test"):
            bot.sende_nachricht("Juhu", id)
        if (nachricht[0] == "/id"):
            bot.sende_nachricht(str(id), id)
