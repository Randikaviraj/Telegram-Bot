import os
import telebot


API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Hello'])
def sayHello(message):
    bot.reply_to(message,"hey I am RandiYa, who are are?")

@bot.message_handler(commands=['Play'])
def sayHello(message):
    bot.send_message(message.chat.id,"What do you want to play?")  
    
bot.polling()
    