# JanisFelixBot

## RELEASE AM 1.12! // BOT LÄUFT STABIL

### Ein mit Python und der vereinfachten Bot-API geschriebener Telegram-Bot.

janisfelixbot: https://telegram.me/janis_felix_bot
beta: https://telegram.me/JanisFelixBetaBot
Webseite: https://JanisFelixBot.tk

Um den Bot zu nutzen musst du die vereinfachte Bot-API installieren, die Felix bearbeitet hat: https://github.com/Flixlix/telegram-chatter und den Anweisungen in admins.txt folgen.

Aktueller Status: Die Entwicklung schreitet gerade ziemlich voran, der Bot läuft jetzt im Uberspace. Er wird 24/7 online sein und selbst wenn er abstürtzt wieder automatisch neugestartet. Release am 1.12.2016!

# Installation

Folgende Python module werden benötigt:
-pyqrcode     
-cleverbot
-image     
-pypng     
-requests     

Diese können mit  ``pip3 install deinmodul`` installiert werden.
## Windows

Vorraussetzung:   
-Python 3

Auf Github drücke auf ``Clone or Download`` und dann auf ``Download ZIP``. Nun gehe auf https://github.com/Flixlix/telegram-chatter und mache das Gleiche. Nun entpacke beide ZIP Dateien und kopiere den Inhalt von ``Downloadverzeichnis\telegram-chatter-master`` in den Ordner ``Downloadverzeichnis\JanisFelixBot-master\JanisFelixBot``. Bearbeite nun Bot.py und füge deinen Bot token ein. Nun trage deine ID in admins.txt ein und starte den Bot!

### Fehlermeldungen

Wenn du ``Traceback (most recent call last):
  File "C:/Users/Janis/Desktop/Bot.py", line 2, in <module>
    from chatter.telegramBot import TelegramBot
  File "C:\python3\chatter\telegramBot.py", line 19, in <module>
    import requests
ImportError: No module named 'requests'`` als Fehlermeldung erhälst, folge diesen Schritten:    
Starte die Eingabeaufforderung (cmd). Gebe nun folgenden Befehl ein:  
``py -3 -m pip install requests``    
Nun starte Bot.py und der Bot sollte funktionieren!

## Ubuntu

Coming soon.
