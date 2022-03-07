#5278901052:AAGtTwYXA7qPF8pYGAzsNzUpIw5fhgiXSSE

import telebot

bot = telebot.TeleBot("5278901052:AAGtTwYXA7qPF8pYGAzsNzUpIw5fhgiXSSE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello! How are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
#	bot.reply_to(message, message.text)
	if message.text == 'Привет' or 'привет':
		bot.reply_to(message, 'Здраствуйте!')
	elif message.text == '/reg':
	bot.reply_to(message, f"Name: {message.from_}")
	bot.reply_to(message, "Hello! How are you doing?")
	else:
		bot.reply_to(message, 'invalid value')

bot.infinity_polling()