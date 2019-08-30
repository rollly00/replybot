import telebot
import logging

bot = telebot.TeleBot("TOKEN")
ids = [1234567]
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	username = message.from_user.username
	first = str(message.from_user.first_name) + " " + str(message.from_user.last_name)
	
	if message.chat.id in ids:
		bot.send_message(*CHATID*,message.text + "\nFrom:@" + username + "\n" + first)
	else:
		pass

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot.polling()