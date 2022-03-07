import telebot
from telebot import types
name=''
surname=''
age=0
bot  =  telebot . TeleBot ( "5250766987:AAG_AFUmbHY9Gf8PNYSGIdvrg2-v-fGm1bc" , parse_mode = None )
keyboard=types.InlineKeyboardMarkup()
keyboard_1adress=types.InlineKeyboardButton(text='Youtube',callback_data='adress1')
keyboard_2adress=types.InlineKeyboardButton(text='Twitch',callback_data='adress2')
keyboard.add(keyboard_1adress,keyboard_2adress)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id,text="Hello, where you want registered",  reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call:True)
def check(call):
	if  call . data == 'address1' :
		bot.send_message(call.message.chat.id, "You're register in Youtube. Write your name")
		bot.register_next_step_handler(call.message, register_name)
	elif  call . data == 'adress2' :
		bot.send_message(call.message.chat.id, "You're register in Twitch. Write your name")
		bot.register_next_step_handler(call.message.chat.id, register_name)
@bot.nessage_handler(func=lambda m:True)
def register_name(message):
	bot
	global name
	name=message.chat.id

bot.infinity_polling()
