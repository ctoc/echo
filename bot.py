# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:04:40 2017

@author: dant
"""

   
    
# -*- coding: utf-8 -*-
import config
import telebot
import urllib3

urllib3.disable_warnings()
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
bot.polling(none_stop=True)