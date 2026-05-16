import telebot 
from transliterate import to_latin, to_cyrillic
from dotenv import load_dotenv
from transliterate import to_latin, to_cyrillic

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu aleykum xush kelibsiz! Sizga qanday yozdam kerak?")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	text=message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else:
	    bot.reply_to(message,to_latin(text))  


bot.infinity_polling()

