import telebot 
from decouple import config

token = config('TOKEN')

# stikers
yes_stickers = "CAACAgIAAxkBAAEIBWpkBYbMENVV6_6pqSzH237_cMYKbAACuQMAAnwFBxtmpcR-eeNqWC4E"
no_stickers = "CAACAgIAAxkBAAEIBXNkBYbTAq_LEQi8WLzlnd0UjyYE1AACuAMAAnwFBxsVPZxxpEY-hi4E"

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1, b2)




bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопу', reply_markup=keyboard)


# func - функция фильтр, в данном случае разрешаются все сообщения
@bot.callback_query_handler(func=lambda x: True)

def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_stickers)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_stickers)


bot.polling()



