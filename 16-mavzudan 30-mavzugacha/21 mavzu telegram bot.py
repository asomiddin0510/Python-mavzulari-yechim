
from pyexpat.errors import messages
from xml.sax import parse
from transliterate import to_latin, to_cyrillic

import telebot

TOKEN = "7654650202:AAFdP5j0bOVoQbfVr_iCUKwZIru9AWqujQI"



bot = telebot.TeleBot(TOKEN, parse_mode =  None)

@bot.message_handler(commands=['start'])
def send_welcome(message):

    javob = "Assalomu alaykum . Xush kelibsiz! "
    javob += "\nMatn kiriting: "

    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)

def modification(message) :
    msg = message.text

    if msg.isascii() :
        javob = to_cyrillic(msg)
        print(javob)

    else:
        javob = to_latin(msg)
        print(javob)

    bot.reply_to(message, javob)



bot.polling()










































