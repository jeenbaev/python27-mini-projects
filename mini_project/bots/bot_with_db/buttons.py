from telebot import types
from utils import get_pages

Keyboard = types.InlineKeyboardMarkup()

pages = get_pages()
buttons = []
for page in pages:
    b = types.InlineKeyboardButton(page, callback_data=page)
    buttons.append(b)
    
Keyboard.add(*buttons)




