import telebot 
from decouple import config

token = config('TOKEN')

# stikers
yes_stikers = "CAACAgIAAxkBAAEIBWpkBYbMENVV6_6pqSzH237_cMYKbAACuQMAAnwFBxtmpcR-eeNqWC4E"
no_stikers = "CAACAgIAAxkBAAEIBXNkBYbTAq_LEQi8WLzlnd0UjyYE1AACuAMAAnwFBxsVPZxxpEY-hi4E"

bot = telebot.TeleBot(token)

# buttons

keyboard = telebot.types.ReplyKeyboardMarkup() # (one_time_keyboard=True)
b1 = telebot.types.KeyboardButton('хуесос')
b2 = telebot.types.KeyboardButton('пиздабол')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Аза хуесос или пиздабол?', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'хуесос':
        bot.send_sticker(message.chat.id, yes_stikers)
    elif message.text == 'пиздабол':
        bot.send_sticker(message.chat.id, no_stikers)
    else:
        bot.send_message(message.chat.id, "Просто выбери что считаешь..")
    
    bot.register_next_step_handler(message, reply_to_button)




bot.polling()
