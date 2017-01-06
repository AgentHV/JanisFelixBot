# JanisFelixBot

## VIELE NEUE FUNKTIONEN: MEHR AUF JANISFELIXBOT.TK!

### Ein mit Python und der vereinfachten Bot-API geschriebener Telegram-Bot.

janisfelixbot: https://telegram.me/janis_felix_bot
beta: https://telegram.me/JanisFelixBetaBot
Webseite: https://JanisFelixBot.tk


# Installation

Python 3 wird vorausgesetzt.

Folgende Python module werden benötigt:     
-pyqrcode     
-cleverbot   
-image     
-requests   
-telegraph   
-regex   
-pyshorteners   

Diese können mit  ``pip3 install deinmodul`` installiert werden.

1. Auf Github drücke auf ``Clone or Download`` und dann auf ``Download ZIP``. Nun gehe auf https://github.com/Flixlix/telegram-chatter und mache das Gleiche. Nun entpacke beide ZIP Dateien und kopiere den Inhalt von ``Downloadverzeichnis\telegram-chatter-master`` in den Ordner ``Downloadverzeichnis\JanisFelixBot-master\JanisFelixBot``.
2. Um den Bot zu nutzen musst du die vereinfachte Bot-API installieren, die Felix bearbeitet hat: https://github.com/Flixlix/telegram-chatter.   
3. Ersetze nun die folgende Werte direkt am Anfang der Bot.py:   
`bot = TelegramBot("`Hier muss dein Telegram Bot-Token rein`")`   
`api_key = "`Hier muss dein Token der goo.gl API rein`"`   
`admingroup = `Hier muss die ID der Admingruppe rein   
  In die Admingruppe sendet der Bot Nachrichten wenn ein Nicht-Admin probiert etwas für Admins auszuführen.
4. Nun ersetze den Text der admins.txt mit deiner ID. Später können per /addadmin mehr Admins hinzugefügt werden.  

### Fehlermeldungen

Wenn du ``Traceback (most recent call last):
  File "C:/Users/username/Desktop/Bot.py", line 2, in <module>
    from chatter.telegramBot import TelegramBot
  File "C:\python3\chatter\telegramBot.py", line 19, in <module>
    import requests
ImportError: No module named 'requests'`` als Fehlermeldung erhälst, folge diesen Schritten (nur Windows):    
Starte die Eingabeaufforderung (cmd). Gebe nun folgenden Befehl ein:  
``py -3 -m pip install requests``    
Nun starte Bot.py und der Bot sollte funktionieren!

