import telebot
from decouple import config


token = config('TOKEN')


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(892891195, 'Hello')
# bot.polling()


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])            # message_handler - обработчик сообщений
def start_message(message):
    bot.send_message(message.chat.id, "Hello bbaby")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHPpBjwli84_zkq7hcPdFQ8qJHvlfElwACHgADjxZpNE5t1AT5S-neLQQ')
    bot.send_photo(message.chat.id, 'https://unsplash.com/photos/F_-0BxGuVvo')

@bot.message_handler(content_types=['text'])
def ggg(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')

@bot.message_handler(content_types=['sticker'])
def ghj(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)




bot.polling()


